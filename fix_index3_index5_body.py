import re

for file in ['index3.html', 'index5.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    badges_html = """
    <!-- Compliance Badges -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-10">
        <div class="mt-8 pt-8 border-t border-slate-200/60 flex flex-wrap gap-4 justify-center md:justify-start">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 border border-slate-200 text-slate-700 text-xs font-bold">
                <i class="fas fa-shield-alt text-brand-blue"></i> Fully GDPR compliant
            </div>
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 border border-slate-200 text-slate-700 text-xs font-bold">
                <i class="fas fa-globe-europe text-brand-teal"></i> Hosted in the EU
            </div>
        </div>
    </div>
"""

    if 'GDPR compliant' not in content:
        # Check if </body> exists
        if '</body>' in content:
            # We want to inject it before <script src="./js/main.js"></script> or </body>
            # Usually there is an ending </section> tag
            new_content = re.sub(r'(<!-- SCRIPTS -->|</body>)', badges_html + r'\n    \1', content, count=1)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added badges to {file}")
