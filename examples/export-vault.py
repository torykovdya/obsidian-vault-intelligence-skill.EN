#!/usr/bin/env python3
"""
export-vault.py — Obsidian Vault Exporter for Vault Intelligence analysis

Usage:
    python3 export-vault.py ~/ObsidianVault > vault-export.txt
    python3 export-vault.py ~/ObsidianVault --folder "10-Permanent" > permanent-only.txt
    python3 export-vault.py ~/ObsidianVault --days 30 > last-month.txt
    python3 export-vault.py ~/ObsidianVault --stats

Windows:
    python export-vault.py "C:\\Users\\Name\\ObsidianVault" > vault-export.txt
    python export-vault.py "%USERPROFILE%\\ObsidianVault" > vault-export.txt

Then copy the contents of vault-export.txt into Claude.
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime, timedelta


def parse_args():
    parser = argparse.ArgumentParser(
        description="Экспорт Obsidian vault для анализа в Claude"
    )
    parser.add_argument("vault_path", help="Path to your Obsidian vault")
    parser.add_argument(
        "--folder", 
        help="Экспортировать только конкретную папку (например: '10-Permanent')",
        default=None
    )
    parser.add_argument(
        "--days",
        type=int,
        help="Экспортировать только заметки за последние N дней",
        default=None
    )
    parser.add_argument(
        "--exclude",
        nargs="+",
        help="Исключить папки (например: --exclude Archive Templates)",
        default=["Archive", "Templates", ".obsidian", "assets"]
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Показать статистику vault вместо экспорта"
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        help="Maximum number of characters in the export (default: 200000)",
        default=200_000
    )
    return parser.parse_args()


def should_include(file_path: Path, args, vault_root: Path) -> bool:
    """Проверяет, нужно ли включать файл в экспорт."""
    relative = file_path.relative_to(vault_root)
    parts = relative.parts
    
    # Исключить папки из --exclude
    for excluded in args.exclude:
        if excluded in parts:
            return False
    
    # Фильтр по папке
    if args.folder and args.folder not in str(relative):
        return False
    
    # Фильтр по дате
    if args.days:
        cutoff = datetime.now() - timedelta(days=args.days)
        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        if mtime < cutoff:
            return False
    
    return True


def export_vault(vault_path: str, args) -> str:
    """Collects vault contents into a single text block."""
    # Supports Windows paths and environment variables
    vault = Path(os.path.expandvars(vault_path)).expanduser().resolve()
    
    if not vault.exists():
        print(f"Error: folder not found: {vault}", file=sys.stderr)
        sys.exit(1)
    
    md_files = sorted(vault.rglob("*.md"))
    included_files = [f for f in md_files if should_include(f, args, vault)]
    
    output_parts = []
    total_chars = 0
    included_count = 0
    skipped_count = 0
    
    # Заголовок экспорта
    header = f"""=== OBSIDIAN VAULT EXPORT ===
Vault: {vault.name}
Exported: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Total files found: {len(md_files)}
Files included: {len(included_files)}
Filter: folder={args.folder or 'all'}, days={args.days or 'all'}
===========================

"""
    output_parts.append(header)
    total_chars += len(header)
    
    for file_path in included_files:
        try:
            content = file_path.read_text(encoding="utf-8")
            if not content.strip():
                continue
            
            relative = file_path.relative_to(vault)
            mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            
            file_block = f"""
--- NOTE ---
Path: {relative}
Modified: {mtime.strftime('%Y-%m-%d')}
---
{content.strip()}
--- END NOTE ---

"""
            
            if total_chars + len(file_block) > args.max_chars:
                skipped_count += 1
                continue
            
            output_parts.append(file_block)
            total_chars += len(file_block)
            included_count += 1
            
        except Exception as e:
            print(f"Could not read {file_path}: {e}", file=sys.stderr)
    
    if skipped_count > 0:
        output_parts.append(f"\n[Skipped {skipped_count} files due to the {args.max_chars}-character limit. Use --folder to narrow the export.]\n")
    
    footer = f"\n=== END OF EXPORT: {included_count} notes, ~{total_chars} characters ===\n"
    output_parts.append(footer)
    
    return "".join(output_parts)


def show_stats(vault_path: str, args):
    """Shows vault statistics."""
    vault = Path(os.path.expandvars(vault_path)).expanduser().resolve()
    md_files = list(vault.rglob("*.md"))
    
    # Статистика по папкам
    folder_counts = {}
    total_chars = 0
    orphan_candidates = []
    
    for f in md_files:
        relative = f.relative_to(vault)
        folder = str(relative.parent) if relative.parent != Path(".") else "(root)"
        folder_counts[folder] = folder_counts.get(folder, 0) + 1
        
        try:
            content = f.read_text(encoding="utf-8")
            total_chars += len(content)
            # Простая проверка на orphan (нет [[ссылок]])
            if "[[" not in content:
                orphan_candidates.append(str(relative))
        except:
            pass
    
    print(f"\n📊 VAULT STATISTICS: {vault.name}")
    print(f"{'='*50}")
    print(f"Total notes:        {len(md_files)}")
    print(f"Total characters:   ~{total_chars:,}")
    print(f"Orphan notes:       {len(orphan_candidates)} (no [[links]])")
    print(f"\n📁 FOLDERS:")
    for folder, count in sorted(folder_counts.items(), key=lambda x: -x[1])[:15]:
        bar = "█" * min(count, 30)
        print(f"  {folder:<35} {bar} {count}")
    
    if orphan_candidates[:5]:
        print(f"\n⚠️  ORPHAN NOTE EXAMPLES (first 5):")
        for note in orphan_candidates[:5]:
            print(f"  - {note}")
    
    print(f"\n💡 To analyze in Claude:")
    print(f"  python3 export-vault.py {vault_path} > vault-export.txt")
    print(f"  Estimated size: ~{total_chars:,} characters")
    if total_chars > 200_000:
        print(f"  ⚠️  Vault is large. Recommended: --folder '10-Permanent' --days 90")


def main():
    args = parse_args()
    
    if args.stats:
        show_stats(args.vault_path, args)
    else:
        result = export_vault(args.vault_path, args)
        print(result)


if __name__ == "__main__":
    main()
