import glob
import re

html_files = glob.glob('*.html')

badges_html = """
                <!-- Compliance Badges -->
                <div class="mt-8 pt-8 border-t border-slate-200/60 flex flex-wrap gap-4 justify-center md:justify-start">
                    <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 border border-slate-200 text-slate-700 text-xs font-bold">
                        <i class="fas fa-shield-alt text-brand-blue"></i> Fully GDPR compliant
                    </div>
                    <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 border border-slate-200 text-slate-700 text-xs font-bold">
                        <i class="fas fa-globe-europe text-brand-teal"></i> Hosted in the EU
                    </div>
                </div>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to insert the badges in the footer.
    # Looking at the index.html structure, the footer has:
    # </div>
    # </div>
    # </footer>

    # Let's find the closing tag of the main footer container.
    # Usually it's right before </footer>
    # Let's try replacing "        </div>\n    </footer>" with the badges and then the closing div and footer

    # Or more robustly, find `</footer>` and insert it just inside the last div inside the footer.

    # Let's try to find the copyright section to insert it right before that, or at the end of the footer.
    # We will inject it just before the `</footer>` tag, but inside a container if possible.
    # The structure usually has `<div class="pt-8 border-t border-slate-200/60 flex flex-col md:flex-row justify-between items-center gap-4">` at the bottom.

    # Let's just insert it right before `</footer>`
    if 'GDPR compliant' not in content:
        # We need to make sure we don't mess up the HTML structure, so we insert it before the closing footer tag.
        # It's better to insert it right before the closing </footer>
        new_content = re.sub(r'(</footer>)', badges_html + r'\n    \1', content)

        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added badges to {file}")
