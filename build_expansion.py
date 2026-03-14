"""
MzansiWins Site Expansion - New Category Pages
Generates: sport pages, comparison pages, payment-by-method pages, guides,
quiz, bonus finder, author pages, and casino equivalents.
Called from build_site.py after the main build.
"""
import json, os, random
from html import escape as _e

def e(s):
    return _e(str(s)) if s else ''

# ---------------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------------
with open(os.path.join(os.path.dirname(__file__), 'site_expansion_data.json')) as f:
    EXPANSION = json.load(f)

AUTHORS = EXPANSION['authors']
AUTHORS_MAP = {a['id']: a for a in AUTHORS}

# Author photo mapping
AUTHOR_PHOTOS = {
    'Thabo Mokoena': 'author-thabo-mokoena.jpg',
    'Lerato Dlamini': 'author-lerato-dlamini.jpg',
    'Sipho Nkosi': 'author-sipho-nkosi.jpg',
    'Naledi Khumalo': 'author-naledi-khumalo.jpg',
}
AUTHOR_NAMES_LIST = ['Thabo Mokoena', 'Sipho Nkosi', 'Lerato Dlamini', 'Naledi Khumalo']
def get_review_author(brand_id):
    idx = sum(ord(c) for c in brand_id) % len(AUTHOR_NAMES_LIST)
    return AUTHOR_NAMES_LIST[idx]
def author_img_tag(name, size=80, depth=0):
    prefix = '../' * depth
    photo = AUTHOR_PHOTOS.get(name)
    if photo:
        return f'<img src="{prefix}assets/{photo}" alt="{e(name)}" width="{size}" height="{size}" style="width:{size}px;height:{size}px;border-radius:50%;object-fit:cover;object-position:center 20%;flex-shrink:0" loading="lazy">'
    initials = ''.join(w[0] for w in name.split()[:2]).upper() if name else 'MW'
    return f'<div style="width:{size}px;height:{size}px;border-radius:50%;background:#1641B4;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:{max(size//3,12)}px;flex-shrink:0">{initials}</div>'
BETTING_GUIDES = EXPANSION['betting_guides']
CASINO_GUIDES = EXPANSION['casino_guides']
COMPARISONS_BETTING = EXPANSION['comparisons_betting']
COMPARISONS_CASINO = EXPANSION['comparisons_casino']
PAYMENT_METHOD_PAGES_DATA = EXPANSION['payment_method_pages']


def run_expansion(DATA, BRANDS, BRANDS_ORDERED, page_fn, breadcrumbs_fn, logo_path_fn,
                  masked_exit_fn, brand_bg_fn, rating_badge_fn, write_file_fn,
                  OUT, BASE_URL, ICON_CHECK, ICON_X, ICON_TROPHY, ICON_GIFT,
                  ICON_SHIELD, ICON_CHEVRON_RIGHT, ICON_CHEVRON_DOWN, ICON_STAR,
                  ICON_ARROW_LEFT, category_hero_fn=None, news_sidebar_top5_fn=None):
    """Build all expansion pages. Returns list of (url_path, priority) for sitemap."""
    sitemap_entries = []
    os.makedirs(f'{OUT}/betting', exist_ok=True)
    os.makedirs(f'{OUT}/casino', exist_ok=True)
    os.makedirs(f'{OUT}/guides', exist_ok=True)
    os.makedirs(f'{OUT}/casino-guides', exist_ok=True)
    os.makedirs(f'{OUT}/compare', exist_ok=True)
    os.makedirs(f'{OUT}/authors', exist_ok=True)