"""
SEO content sections for the Best Casino Sites page.
Returns HTML fragments for above-table intro and below-table content.
"""

def casino_sites_intro_html():
    """Return a short, crisp opening line above the table."""
    return '''
    <div class="seo-intro" style="margin-bottom:24px">
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary)">
        The top-rated online casinos for SA players in 2026 - ranked by game selection, payout speed and bonus value. All tested with real rands.
      </p>
    </div>
    '''


def casino_sites_below_table_html(brands_data):
    """Return all the SEO content HTML that goes below the table.
    brands_data is a list of brand dicts sorted by overallRating desc.
    """

    top5_html = _build_top5_casino_reviews(brands_data)
    features_html = _build_key_features()
    legality_html = _build_casino_legality()
    what_makes_good_html = _build_what_makes_good()
    payments_html = _build_casino_payments()
    games_html = _build_casino_games()
    bonuses_html = _build_casino_bonuses()
    mobile_html = _build_mobile_casino()
    faq_html = _build_casino_faq()
    responsible_html = _build_casino_responsible_gambling()

    casino_overview = '''
      <div style="margin-bottom:32px">
        <h2 style="font-size:1.25rem;font-weight:700;color:var(--text-primary);margin-bottom:12px">Online Casinos in South Africa - The Full Picture</h2>
        <p style="font-size:15px;line-height:1.8;color:var(--text-secondary);margin-bottom:16px">
          Online casino gaming has grown rapidly in South Africa as players increasingly access
          gambling platforms via mobile devices. However, the legal environment is complex. While
          sports betting is clearly licensed by provincial gambling authorities, most online casinos
          available to South African players operate from international jurisdictions rather than
          domestic licences.
        </p>
        <p style="font-size:15px;line-height:1.8;color:var(--text-secondary)">
          Despite this, millions of South Africans still play at reputable casino sites that support
          local payment methods, offer games in South African Rand (ZAR), and provide fast withdrawals.
          Below we break down how they work, how to choose a safe platform, and what features matter
          most for South African players.
        </p>
      </div>
    '''

    return f'''
    <div class="seo-below-table" style="margin-top:56px">
      {casino_overview}
      {top5_html}
      {features_html}
      {legality_html}
      {what_makes_good_html}
      {payments_html}
      {games_html}
      {bonuses_html}
      {mobile_html}
      {faq_html}
      {responsible_html}
    </div>
    '''


def _casino_review_card(brand, rank, summary, pros, cons, verdict):
    """Build a mini review card for a casino brand."""
    import html as h
    name = h.escape(brand.get('name', ''))
    bonus = h.escape(brand.get('welcomeBonusAmount', ''))
    rating = float(brand.get('overallRating', 0))
    rating_str = f'{rating:.1f}'
    bid = brand['id']

    pros_li = ''.join(f'<li>{p}</li>' for p in pros)
    cons_li = ''.join(f'<li>{c}</li>' for c in cons)

    return f'''
    <div class="seo-review-card" style="border:1px solid var(--border);border-radius:12px;padding:28px;margin-bottom:24px;background:var(--card-bg)">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:16px">
        <div style="display:flex;align-items:center;gap:12px">
          <span style="font-size:22px;font-weight:800;color:var(--accent)">#{rank}</span>
          <a href="betting-site-review/{bid}.html" style="font-size:20px;font-weight:700;color:var(--text-primary);text-decoration:none">{name}</a>
        </div>
        <span class="rating-badge {'high' if rating >= 4.2 else 'mid' if rating >= 3.5 else 'low'} sm">{rating_str}/5.0</span>
      </div>
      <p style="font-size:16px;font-weight:700;color:var(--bonus);margin-bottom:16px">{bonus}</p>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:20px">{summary}</p>
      <div class="seo-pros-cons">
        <div>
          <p style="font-size:13px;font-weight:700;color:var(--bonus);margin-bottom:8px;text-transform:uppercase;letter-spacing:0.5px">What we like</p>
          <ul style="list-style:none;padding:0;margin:0">{pros_li}</ul>
        </div>
        <div>
          <p style="font-size:13px;font-weight:700;color:#dc2626;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.5px">Could be better</p>
          <ul style="list-style:none;padding:0;margin:0">{cons_li}</ul>
        </div>
      </div>
      <p style="font-size:14px;line-height:1.75;color:var(--text-muted);font-style:italic;border-top:1px solid var(--sep);padding-top:16px;margin:0">
        <strong style="color:var(--text-primary)">Our verdict:</strong> {verdict}
      </p>
      <div style="margin-top:16px;display:flex;gap:12px;flex-wrap:wrap">
        <a href="betting-site-review/{bid}.html" class="btn-outline btn-sm">Full review</a>
        <a href="promo-code/{bid}.html" class="btn-outline btn-sm" style="border-color:var(--bonus);color:var(--bonus)">Promo code</a>
      </div>
    </div>
    '''


def _build_top5_casino_reviews(brands_data):
    """Build the top 5 casino reviews section using brands that have casino products."""
    brand_map = {b['id']: b for b in brands_data}

    # Top 5 casino-relevant brands: Jackpot City (pure casino), then top-rated brands with strong casino offerings
    review_order = ['jackpot-city', 'betway-south-africa', 'hollywoodbets', 'playtsogo', 'betfred']
    review_brands = [brand_map[bid] for bid in review_order if bid in brand_map]

    reviews_data = [
        {
            'summary': 'Jackpot City is one of the few pure casino brands available to South African players. Their massive slot library includes hundreds of titles from top providers, plus progressive jackpots that regularly pay out life-changing sums. The 100% match bonus up to R4,000 plus spins gives you a solid bankroll to start with.',
            'pros': ['Dedicated casino platform - not an afterthought', 'Huge slot library with progressive jackpots', 'Supports ZAR deposits and withdrawals', 'Strong reputation built over years of operation'],
            'cons': ['Not licensed by a South African provincial board', 'Sports betting not available', 'Withdrawal processing can be slower than local operators'],
            'verdict': 'If you are after a pure casino experience with a massive game library, Jackpot City is hard to beat. The welcome bonus is fair, the game selection is enormous, and they have been around long enough to trust with your rands.'
        },
        {
            'summary': 'Betway is best known for sports betting, but their casino section is genuinely impressive. You get access to blackjack, roulette, live dealer games, slots, and crash games like Aviator - all under one roof. The R10 free bet and 10 Aviator flights welcome package lets you test both the sportsbook and casino without much risk.',
            'pros': ['Trusted global brand with SA licence', 'Combined sports and casino in one account', 'Excellent live dealer game selection', 'Fast withdrawals via Instant EFT'],
            'cons': ['Casino bonus is modest compared to pure casino sites', 'Slot library smaller than dedicated casino platforms'],
            'verdict': 'Betway is the best choice if you want sports betting and casino gaming in one place. The live dealer games are top-tier, and knowing your money is with a licensed SA operator gives real peace of mind.'
        },
        {
            'summary': 'Hollywoodbets is South Africa through and through. Their Spina Zonke casino games have become a cultural phenomenon, and the R25 free bonus plus 50 spins on sign-up means you can spin the reels without depositing a cent. Add in Aviator, JetX, and hundreds of slots, and the casino offering is surprisingly strong for what started as a sports bookmaker.',
            'pros': ['No deposit needed for R25 free bonus + 50 spins', 'Spina Zonke games are uniquely popular in SA', 'Physical branches for in-person support', 'R5 minimum deposit - the lowest around'],
            'cons': ['Casino game variety is smaller than international operators', 'No traditional table games like blackjack or roulette'],
            'verdict': 'Hollywoodbets is the go-to for casual casino players who want to spin for fun without any risk. The no-deposit bonus and Spina Zonke exclusives make it uniquely South African.'
        },
        {
            'summary': 'PlayTsogo brings the Tsogo Sun casino brand online with slots, table games, and live dealer options. Their massive R10,000 welcome package plus 25 bet credits, 50 spins, and 25 Aviator flights is one of the most generous in the market. The live dealer games connect you to professional studios for an authentic casino floor experience.',
            'pros': ['Backed by Tsogo Sun - a trusted SA casino group', 'Huge R10,000+ welcome package', 'Full range: slots, table games, live dealer', 'Aviator and crash games included'],
            'cons': ['Platform can feel cluttered with so many options', 'Brand is still building its online reputation'],
            'verdict': 'PlayTsogo is the best pick if you want a land-based casino feel online. The Tsogo Sun backing means quality games and proper regulation, and that welcome package is hard to ignore.'
        },
        {
            'summary': 'Betfred brings decades of UK gambling experience to South Africa with a casino offering that punches well above its weight. The headline number is staggering - up to R21,000 plus 750 spins spread across your first deposits. Their casino includes a wide range of slots, table games, and live dealer options from top-tier game providers.',
            'pros': ['Biggest combined bonus in SA - R21,000 + 750 spins', 'Decades of UK gambling pedigree', 'Strong slot and live dealer selection', 'Progressive jackpots available'],
            'cons': ['Bonus is spread across multiple deposits', 'Not as well-known in SA as local brands', 'Wagering requirements on the full bonus are high'],
            'verdict': 'If you are chasing the biggest bonus number, Betfred is your pick. The R21,000 headline is real, though you will need multiple deposits to unlock it all. The casino game quality is excellent.'
        },
    ]

    cards = ''
    for i, (brand, data) in enumerate(zip(review_brands, reviews_data)):
        cards += _casino_review_card(brand, i + 1, data['summary'], data['pros'], data['cons'], data['verdict'])

    return f'''
    <div class="seo-section" style="margin-bottom:48px">
      <h2 style="font-size:1.5rem;font-weight:700;color:var(--text-primary);margin-bottom:8px">Top 5 Online Casino Sites for SA Players - Reviewed</h2>
      <p style="font-size:15px;color:var(--text-muted);margin-bottom:24px;line-height:1.75">
        We tested each of these casino platforms with real money - depositing, playing, and withdrawing
        in South African Rand. Here is what we found.
      </p>
      {cards}
    </div>
    '''


def _build_key_features():
    """Build the key features section."""
    return '''
    <div class="seo-section" style="margin-bottom:48px">
      <h2 style="font-size:1.5rem;font-weight:700;color:var(--text-primary);margin-bottom:16px">What the Best Casino Sites Have in Common</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:16px">
        <div style="border:1px solid var(--border);border-radius:10px;padding:20px;background:var(--card-bg);text-align:center">
          <div style="font-size:28px;margin-bottom:8px">R</div>
          <p style="font-weight:700;color:var(--text-primary);margin-bottom:4px;font-size:15px">ZAR Support</p>
          <p style="font-size:13px;color:var(--text-secondary);line-height:1.6;margin:0">
            Deposits and withdrawals in South African Rand - no conversion fees.
          </p>
        </div>
        <div style="border:1px solid var(--border);border-radius:10px;padding:20px;background:var(--card-bg);text-align:center">
          <div style="font-size:28px;margin-bottom:8px">&#9889;</div>
          <p style="font-weight:700;color:var(--text-primary);margin-bottom:4px;font-size:15px">Fast Verification</p>
          <p style="font-size:13px;color:var(--text-secondary);line-height:1.6;margin:0">
            Quick KYC and FICA checks so you can start playing and withdrawing sooner.
          </p>
        </div>
        <div style="border:1px solid var(--border);border-radius:10px;padding:20px;background:var(--card-bg);text-align:center">
          <div style="font-size:28px;margin-bottom:8px">&#127922;</div>
          <p style="font-weight:700;color:var(--text-primary);margin-bottom:4px;font-size:15px">Game Variety</p>
          <p style="font-size:13px;color:var(--text-secondary);line-height:1.6;margin:0">
            Hundreds of slots, live dealer games, table games, and crash games.
          </p>
        </div>
        <div style="border:1px solid var(--border);border-radius:10px;padding:20px;background:var(--card-bg);text-align:center">
          <div style="font-size:28px;margin-bottom:8px">&#128241;</div>
          <p style="font-weight:700;color:var(--text-primary);margin-bottom:4px;font-size:15px">Mobile-Optimised</p>
          <p style="font-size:13px;color:var(--text-secondary);line-height:1.6;margin:0">
            Play on any device - responsive design that works on Android and iOS.
          </p>
        </div>
      </div>
    </div>
    '''


def _build_casino_legality():
    """Build the legality section for casino."""
    return '''
    <div class="seo-section" style="margin-bottom:48px">
      <h2 style="font-size:1.5rem;font-weight:700;color:var(--text-primary);margin-bottom:16px">Is Online Casino Gambling Legal in South Africa?</h2>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:16px">
        South Africa has one of the most unusual gambling frameworks in the world. The short answer
        is: it is complicated.
      </p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:16px;margin-bottom:20px">
        <div style="border-left:4px solid var(--bonus);border-radius:0 10px 10px 0;padding:20px;background:var(--card-bg);border:1px solid var(--border);border-left:4px solid var(--bonus)">
          <p style="font-weight:700;color:var(--text-primary);margin-bottom:6px">Sports Betting</p>
          <p style="font-size:14px;color:var(--text-secondary);line-height:1.75;margin:0">
            Fully legal through operators licensed by provincial gambling boards. All sports bookmakers
            on this site hold valid SA licences.
          </p>
        </div>
        <div style="border-left:4px solid #f59e0b;border-radius:0 10px 10px 0;padding:20px;background:var(--card-bg);border:1px solid var(--border);border-left:4px solid #f59e0b">
          <p style="font-weight:700;color:var(--text-primary);margin-bottom:6px">Online Casino Games</p>
          <p style="font-size:14px;color:var(--text-secondary);line-height:1.75;margin:0">
            Traditional casino games like slots, blackjack, and roulette are not fully licensed
            domestically. Many platforms accepting SA players operate from offshore licences.
          </p>
        </div>
        <div style="border-left:4px solid var(--accent);border-radius:0 10px 10px 0;padding:20px;background:var(--card-bg);border:1px solid var(--border);border-left:4px solid var(--accent)">
          <p style="font-weight:700;color:var(--text-primary);margin-bottom:6px">What This Means for You</p>
          <p style="font-size:14px;color:var(--text-secondary);line-height:1.75;margin:0">
            In practice, millions of South Africans play at reputable international casino platforms
            that accept SA customers and support Rand payments. The National Gambling Board oversees
            regulation nationally.
          </p>
        </div>
      </div>
      <div style="background:var(--surface);border-radius:10px;padding:20px;border:1px solid var(--border)">
        <p style="font-size:14px;line-height:1.75;color:var(--text-secondary);margin:0">
          <strong style="color:var(--text-primary)">Our advice:</strong>
          Stick to platforms that hold recognised international licences (Malta Gaming Authority,
          UK Gambling Commission, or Curacao eGaming), support ZAR payments, and have a track record
          of paying out to South African players. All casino sites listed on this page meet these criteria.
        </p>
      </div>
    </div>
    '''


def _build_what_makes_good():
    """Build the 'what makes a good casino' section with licensing and security."""
    return '''
    <div class="seo-section" style="margin-bottom:48px">
      <h2 style="font-size:1.5rem;font-weight:700;color:var(--text-primary);margin-bottom:16px">What Makes a Good Online Casino in South Africa?</h2>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:20px">
        Ranking high-quality casino sites requires evaluating several factors. Here is what we look
        for when deciding which platforms deserve your trust and your rands.
      </p>

      <h3 style="font-size:1.125rem;font-weight:700;color:var(--text-primary);margin-bottom:12px">Licensing and Security</h3>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:16px">
        A trustworthy online casino should hold licences from recognised gambling jurisdictions. The
        three most respected are:
      </p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));gap:12px;margin-bottom:20px">
        <div style="border:1px solid var(--border);border-radius:8px;padding:16px;background:var(--card-bg);text-align:center">
          <p style="font-weight:700;color:var(--accent);margin-bottom:4px;font-size:14px">Malta Gaming Authority</p>
          <p style="font-size:12px;color:var(--text-muted);margin:0">(MGA)</p>
        </div>
        <div style="border:1px solid var(--border);border-radius:8px;padding:16px;background:var(--card-bg);text-align:center">
          <p style="font-weight:700;color:var(--accent);margin-bottom:4px;font-size:14px">UK Gambling Commission</p>
          <p style="font-size:12px;color:var(--text-muted);margin:0">(UKGC)</p>
        </div>
        <div style="border:1px solid var(--border);border-radius:8px;padding:16px;background:var(--card-bg);text-align:center">
          <p style="font-weight:700;color:var(--accent);margin-bottom:4px;font-size:14px">Curacao eGaming</p>
          <p style="font-size:12px;color:var(--text-muted);margin:0">(CEG)</p>
        </div>
      </div>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:16px">
        These licences require operators to meet strict standards around player protection, fairness,
        and financial security. Security features you should look for include:
      </p>
      <ul style="padding-left:24px;margin-bottom:20px;font-size:15px;color:var(--text-secondary);line-height:1.75">
        <li>SSL encryption on all transactions</li>
        <li>Secure payment gateways</li>
        <li>Responsible gambling tools (deposit limits, self-exclusion)</li>
        <li>Independent game testing and fairness audits</li>
        <li>KYC and FICA verification procedures</li>
      </ul>
    </div>
    '''


def _build_casino_payments():
    """Build the payment methods section for casino."""
    return '''
    <div class="seo-section" style="margin-bottom:48px">
      <h2 style="font-size:1.5rem;font-weight:700;color:var(--text-primary);margin-bottom:16px">Payment Methods for SA Casino Players</h2>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:20px">
        The best online casinos offer local banking options to make deposits and withdrawals easy.
        Using Rand-based payments avoids currency conversion fees and allows you to withdraw winnings
        faster.
      </p>
      <div style="overflow-x:auto;margin-bottom:20px">
        <table style="width:100%;border-collapse:collapse;font-size:14px">
          <thead>
            <tr style="border-bottom:2px solid var(--border)">
              <th style="text-align:left;padding:12px 16px;font-weight:700;color:var(--text-primary)">Method</th>
              <th style="text-align:left;padding:12px 16px;font-weight:700;color:var(--text-primary)">Deposit Speed</th>
              <th style="text-align:left;padding:12px 16px;font-weight:700;color:var(--text-primary)">Withdrawal Speed</th>
              <th style="text-align:left;padding:12px 16px;font-weight:700;color:var(--text-primary)">Casino Support</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--sep)">
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">Instant EFT</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">Instant</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">1 - 3 business days</td>
              <td style="padding:12px 16px;color:var(--bonus);font-weight:600">Most casinos</td>
            </tr>
            <tr style="border-bottom:1px solid var(--sep)">
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">Ozow</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">Instant</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">1 - 2 business days</td>
              <td style="padding:12px 16px;color:var(--bonus);font-weight:600">Widely supported</td>
            </tr>
            <tr style="border-bottom:1px solid var(--sep)">
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">Visa / Mastercard</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">Instant</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">2 - 5 business days</td>
              <td style="padding:12px 16px;color:var(--bonus);font-weight:600">All casinos</td>
            </tr>
            <tr style="border-bottom:1px solid var(--sep)">
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">OTT / Blu Voucher</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">Instant</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">N/A (deposit only)</td>
              <td style="padding:12px 16px;color:var(--text-muted)">Select casinos</td>
            </tr>
            <tr style="border-bottom:1px solid var(--sep)">
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">Bank Transfer</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">1 - 2 hours</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">1 - 3 business days</td>
              <td style="padding:12px 16px;color:var(--bonus);font-weight:600">All casinos</td>
            </tr>
            <tr>
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">Cryptocurrency</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">10 - 30 minutes</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">Under 1 hour</td>
              <td style="padding:12px 16px;color:var(--text-muted)">International casinos</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="font-size:14px;color:var(--text-muted);line-height:1.75">
        <a href="payment-methods.html" style="color:var(--accent)">See our full payment methods guide</a>
        for detailed comparisons across all SA gambling platforms.
      </p>
    </div>
    '''


def _build_casino_games():
    """Build the casino games section with slot, table, and live dealer subsections."""
    return '''
    <div class="seo-section" style="margin-bottom:48px">
      <h2 style="font-size:1.5rem;font-weight:700;color:var(--text-primary);margin-bottom:16px">Casino Games Available to SA Players</h2>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:24px">
        A strong casino platform should provide hundreds of games across multiple categories.
        Here is what you will find at the best SA casino sites.
      </p>

      <!-- Slots -->
      <div style="border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:20px;background:var(--card-bg)">
        <h3 style="font-size:1.125rem;font-weight:700;color:var(--text-primary);margin-bottom:12px">Slot Games</h3>
        <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:16px">
          Slots dominate online casino gaming in South Africa. They are popular because they offer
          low minimum bets, large progressive jackpots, and fast gameplay. Popular titles include:
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px">
          <span style="background:var(--accent-light);color:var(--accent);padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600">Gates of Olympus</span>
          <span style="background:var(--accent-light);color:var(--accent);padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600">Starburst</span>
          <span style="background:var(--accent-light);color:var(--accent);padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600">Big Bass Bonanza</span>
          <span style="background:var(--accent-light);color:var(--accent);padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600">Book of Dead</span>
          <span style="background:var(--accent-light);color:var(--accent);padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600">Sweet Bonanza</span>
          <span style="background:var(--accent-light);color:var(--accent);padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600">Spina Zonke</span>
        </div>
      </div>

      <!-- Table Games -->
      <div style="border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:20px;background:var(--card-bg)">
        <h3 style="font-size:1.125rem;font-weight:700;color:var(--text-primary);margin-bottom:12px">Table Games</h3>
        <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:16px">
          Classic casino games remain extremely popular among South African players. These games
          generally offer better odds compared with slot machines and appeal to more experienced players.
        </p>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(140px, 1fr));gap:12px">
          <div style="text-align:center;padding:16px;background:var(--surface);border-radius:8px">
            <p style="font-weight:700;color:var(--text-primary);margin:0;font-size:14px">Blackjack</p>
          </div>
          <div style="text-align:center;padding:16px;background:var(--surface);border-radius:8px">
            <p style="font-weight:700;color:var(--text-primary);margin:0;font-size:14px">Roulette</p>
          </div>
          <div style="text-align:center;padding:16px;background:var(--surface);border-radius:8px">
            <p style="font-weight:700;color:var(--text-primary);margin:0;font-size:14px">Baccarat</p>
          </div>
          <div style="text-align:center;padding:16px;background:var(--surface);border-radius:8px">
            <p style="font-weight:700;color:var(--text-primary);margin:0;font-size:14px">Poker</p>
          </div>
        </div>
      </div>

      <!-- Live Dealer -->
      <div style="border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:20px;background:var(--card-bg)">
        <h3 style="font-size:1.125rem;font-weight:700;color:var(--text-primary);margin-bottom:12px">Live Dealer Casinos</h3>
        <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:12px">
          Live dealer games are one of the fastest-growing segments of the online casino industry.
          Players connect to real casinos through live video streams where professional dealers host
          games. These games recreate the experience of land-based casinos while allowing you to
          participate from anywhere in South Africa.
        </p>
        <p style="font-size:14px;color:var(--text-muted);line-height:1.75;margin:0">
          Popular live games: Live Blackjack, Live Roulette, Live Baccarat, Game Shows (Dream Catcher, Crazy Time)
        </p>
      </div>
    </div>
    '''


def _build_casino_bonuses():
    """Build the casino bonuses section."""
    return '''
    <div class="seo-section" style="margin-bottom:48px">
      <h2 style="font-size:1.5rem;font-weight:700;color:var(--text-primary);margin-bottom:16px">Casino Bonuses for South African Players</h2>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:20px">
        Welcome bonuses are a key attraction for new players. Here are the most common types you
        will find at SA-friendly casino sites.
      </p>
      <div style="overflow-x:auto;margin-bottom:20px">
        <table style="width:100%;border-collapse:collapse;font-size:14px">
          <thead>
            <tr style="border-bottom:2px solid var(--border)">
              <th style="text-align:left;padding:12px 16px;font-weight:700;color:var(--text-primary)">Bonus Type</th>
              <th style="text-align:left;padding:12px 16px;font-weight:700;color:var(--text-primary)">How It Works</th>
              <th style="text-align:left;padding:12px 16px;font-weight:700;color:var(--text-primary)">Typical Value</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--sep)">
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">Deposit Match</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">Casino matches your first deposit by a percentage (100%, 150%, etc.)</td>
              <td style="padding:12px 16px;color:var(--bonus);font-weight:600">R1,000 - R21,000</td>
            </tr>
            <tr style="border-bottom:1px solid var(--sep)">
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">Free Spins</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">Free slot spins on selected games - winnings subject to wagering</td>
              <td style="padding:12px 16px;color:var(--bonus);font-weight:600">25 - 750 spins</td>
            </tr>
            <tr style="border-bottom:1px solid var(--sep)">
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">No-Deposit Bonus</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">Free bonus without depositing - sign up and play immediately</td>
              <td style="padding:12px 16px;color:var(--bonus);font-weight:600">R25 - R100</td>
            </tr>
            <tr style="border-bottom:1px solid var(--sep)">
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">Cashback</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">Get a percentage of losses refunded, usually weekly</td>
              <td style="padding:12px 16px;color:var(--bonus);font-weight:600">5% - 20%</td>
            </tr>
            <tr>
              <td style="padding:12px 16px;font-weight:600;color:var(--text-primary)">VIP Rewards</td>
              <td style="padding:12px 16px;color:var(--text-secondary)">Loyalty points, personalised bonuses, and exclusive perks for regulars</td>
              <td style="padding:12px 16px;color:var(--bonus);font-weight:600">Varies</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div style="background:var(--accent-light);border-radius:10px;padding:20px;border-left:4px solid var(--accent)">
        <p style="font-size:14px;line-height:1.75;color:var(--text-secondary);margin:0">
          <strong style="color:var(--text-primary)">Always check wagering requirements.</strong>
          These determine how many times a bonus must be played through before you can withdraw
          winnings. A R1,000 bonus with 30x wagering means you need to wager R30,000 before cashing
          out. Lower wagering requirements are always better.
        </p>
      </div>
    </div>
    '''


def _build_mobile_casino():
    """Build the mobile casino section."""
    return '''
    <div class="seo-section" style="margin-bottom:48px">
      <h2 style="font-size:1.5rem;font-weight:700;color:var(--text-primary);margin-bottom:16px">Mobile Casino Gaming in South Africa</h2>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:16px">
        The vast majority of South African casino players access games via their smartphones. All
        the casino sites we recommend are fully optimised for mobile play - no app download required
        in most cases. Just open the casino in your phone's browser and start playing.
      </p>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:16px">
        What to look for in a good mobile casino:
      </p>
      <ul style="padding-left:24px;font-size:15px;color:var(--text-secondary);line-height:1.75;margin-bottom:16px">
        <li>Responsive design that adapts to your screen size</li>
        <li>Touch-friendly game controls</li>
        <li>Quick loading times even on slower connections</li>
        <li>Full game library available on mobile (not just a reduced selection)</li>
        <li>Easy deposit and withdrawal from your phone</li>
      </ul>
      <p style="font-size:14px;color:var(--text-muted);line-height:1.75">
        Pro tip: Hollywoodbets and Betway both offer dedicated Android apps that you can download
        from their websites. For most other casinos, the mobile browser experience is just as smooth.
      </p>
    </div>
    '''


def _build_casino_faq():
    """Build the FAQ section with accordion items."""
    faqs = [
        (
            "Are online casinos legal in South Africa?",
            "Online sports betting is legal through licensed operators. Online casino gaming occupies a grey area - traditional casino games are not fully licensed domestically, but millions of South Africans play at reputable international platforms that accept ZAR. Stick to licensed, well-known operators for maximum safety."
        ),
        (
            "Which online casino has the biggest bonus for SA players?",
            "Betfred offers the largest combined bonus at up to R21,000 plus 750 free spins spread across your first deposits. For a single deposit match, PlayTsogo offers up to R10,000 plus additional bet credits and spins. Always check wagering requirements before choosing based on bonus size alone."
        ),
        (
            "Can I play casino games for free without depositing?",
            "Yes. Hollywoodbets gives you R25 plus 50 free spins just for signing up - no deposit needed. Easybet offers a free R50, and Playbet gives R50 plus 50 spins. These no-deposit bonuses let you try casino games risk-free before committing your own money."
        ),
        (
            "What are the best slot games at SA online casinos?",
            "Popular slots among South African players include Gates of Olympus, Starburst, Big Bass Bonanza, Book of Dead, and Sweet Bonanza. Hollywoodbets' Spina Zonke games are also hugely popular locally. Most casinos offer hundreds of slot titles from providers like Pragmatic Play, NetEnt, and Microgaming."
        ),
        (
            "How do I deposit at an online casino in South Africa?",
            "Most SA casinos accept Instant EFT, Ozow, Visa/Mastercard, bank transfers, and vouchers (OTT, Blu, 1Voucher). Some international casinos also accept cryptocurrency. Instant EFT is the most popular option because deposits are processed immediately and withdrawals are relatively fast."
        ),
        (
            "How long do casino withdrawals take?",
            "Withdrawal times depend on your payment method. Instant EFT withdrawals typically take 1 to 3 business days, card withdrawals take 2 to 5 days, and cryptocurrency can be under an hour. The casino's processing time is usually 24 hours before the funds are released to your bank."
        ),
        (
            "What is the difference between live dealer and regular casino games?",
            "Regular casino games use random number generators (RNG) to determine outcomes - they are software-based. Live dealer games connect you to a real casino studio via video stream where a human dealer runs the game in real time. Live dealer offers a more immersive experience but typically has higher minimum bets."
        ),
        (
            "Do I need to verify my identity to play at an online casino?",
            "Most casinos let you deposit and play immediately, but you will need to complete identity verification (KYC/FICA) before withdrawing winnings. This requires a photo of your ID document and proof of address. Complete verification early to avoid delays when you want to cash out."
        ),
    ]

    items = ''
    for q, a in faqs:
        items += f'''
        <div class="faq-item">
          <button class="faq-btn" onclick="this.parentElement.classList.toggle('open')">
            <span>{q}</span>
            <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-body">
            <p>{a}</p>
          </div>
        </div>
        '''

    return f'''
    <div class="seo-section" style="margin-bottom:48px">
      <h2 style="font-size:1.5rem;font-weight:700;color:var(--text-primary);margin-bottom:16px">Frequently Asked Questions</h2>
      <div style="display:flex;flex-direction:column;gap:8px">
        {items}
      </div>
    </div>
    '''


def _build_casino_responsible_gambling():
    """Build the responsible gambling section for casino."""
    return '''
    <div class="seo-section" style="margin-bottom:48px;padding:28px;background:var(--surface);border-radius:12px;border:1px solid var(--border)">
      <h2 style="font-size:1.5rem;font-weight:700;color:var(--text-primary);margin-bottom:16px">Responsible Gambling</h2>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:16px">
        Casino games are designed to be entertaining, but they can become a problem if not managed
        responsibly. Set a budget before you play and stick to it. Never chase losses, and remember
        that the house always has an edge.
      </p>
      <p style="font-size:15px;line-height:1.75;color:var(--text-secondary);margin-bottom:20px">
        Every reputable casino platform offers responsible gambling tools including deposit limits,
        loss limits, session time reminders, and self-exclusion options. Use them.
      </p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:12px;margin-bottom:16px">
        <div style="background:var(--card-bg);border-radius:8px;padding:16px;border:1px solid var(--border)">
          <p style="font-weight:700;color:var(--text-primary);margin-bottom:4px;font-size:14px">National Responsible Gambling Programme</p>
          <p style="font-size:14px;color:var(--accent);font-weight:600;margin:0">0800 006 008</p>
          <p style="font-size:12px;color:var(--text-muted);margin:0">(Toll-free, 24/7)</p>
        </div>
        <div style="background:var(--card-bg);border-radius:8px;padding:16px;border:1px solid var(--border)">
          <p style="font-weight:700;color:var(--text-primary);margin-bottom:4px;font-size:14px">Gambling Helpline</p>
          <p style="font-size:14px;color:var(--accent);font-weight:600;margin:0">counsellor@responsiblegambling.co.za</p>
        </div>
        <div style="background:var(--card-bg);border-radius:8px;padding:16px;border:1px solid var(--border)">
          <p style="font-weight:700;color:var(--text-primary);margin-bottom:4px;font-size:14px">Self-Exclusion</p>
          <p style="font-size:13px;color:var(--text-secondary);margin:0">Contact your casino directly to self-exclude for 6 months or longer</p>
        </div>
      </div>
      <p style="font-size:13px;color:var(--text-muted);line-height:1.75;margin:0">
        18+ only. Gambling can be addictive. Please play responsibly. If gambling stops being fun, stop playing.
      </p>
    </div>
    '''
