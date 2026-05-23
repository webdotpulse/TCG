import re

with open('premium-components.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header and footer using regex
header_match = re.search(r'(.*?)(<main.*?>)', content, re.DOTALL)
parts = content.rsplit('</main>', 1)

if header_match and len(parts) == 2:
    header = header_match.group(1) + '<main class="pt-32 pb-24">'
    footer = '\n    </main>' + parts[1]

    kb_content = """
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
            <!-- Header Section with Search -->
            <div class="text-center bg-slate-900 rounded-[2.5rem] p-12 lg:p-20 relative overflow-hidden">
                <div class="absolute top-0 left-0 w-full h-full bg-[url('./assets/images/pattern.svg')] opacity-10"></div>
                <div class="relative z-10 max-w-3xl mx-auto">
                    <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-6">Knowledge Base</h1>
                    <p class="text-lg text-slate-300 mb-10">Find guides, tutorials, and answers to your questions.</p>

                    <div class="relative max-w-2xl mx-auto">
                        <i class="fas fa-search absolute left-6 top-1/2 transform -translate-y-1/2 text-slate-400 text-lg"></i>
                        <input type="text" placeholder="Search for articles..." class="w-full pl-14 pr-6 py-4 rounded-2xl bg-white border-0 shadow-lg text-slate-900 font-medium focus:ring-4 focus:ring-brand-blue/30 outline-none transition-all text-lg">
                    </div>
                </div>
            </div>

            <!-- Categories Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Category 1 -->
                <div class="bg-white p-8 rounded-3xl shadow-sm border border-slate-200/60 hover:shadow-lg transition-all duration-300 group cursor-pointer">
                    <div class="w-14 h-14 bg-brand-blue/10 rounded-2xl flex items-center justify-center text-brand-blue mb-6 group-hover:bg-brand-blue group-hover:text-white transition-colors duration-300">
                        <i class="fas fa-plug text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Getting Started</h3>
                    <p class="text-slate-600 mb-6">Basic guides on how to install and set up your first charging station.</p>
                    <ul class="space-y-3 text-sm font-medium text-slate-600">
                        <li class="flex items-center gap-2 hover:text-brand-blue"><i class="far fa-file-alt text-slate-400"></i> Installation Guide</li>
                        <li class="flex items-center gap-2 hover:text-brand-blue"><i class="far fa-file-alt text-slate-400"></i> Account Creation</li>
                        <li class="flex items-center gap-2 hover:text-brand-blue"><i class="far fa-file-alt text-slate-400"></i> First Charge Walkthrough</li>
                    </ul>
                </div>

                <!-- Category 2 -->
                <div class="bg-white p-8 rounded-3xl shadow-sm border border-slate-200/60 hover:shadow-lg transition-all duration-300 group cursor-pointer">
                    <div class="w-14 h-14 bg-brand-teal/10 rounded-2xl flex items-center justify-center text-brand-teal mb-6 group-hover:bg-brand-teal group-hover:text-white transition-colors duration-300">
                        <i class="fas fa-mobile-alt text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">App & Software</h3>
                    <p class="text-slate-600 mb-6">Learn how to use our mobile application and web dashboard effectively.</p>
                    <ul class="space-y-3 text-sm font-medium text-slate-600">
                        <li class="flex items-center gap-2 hover:text-brand-blue"><i class="far fa-file-alt text-slate-400"></i> Linking your RFID card</li>
                        <li class="flex items-center gap-2 hover:text-brand-blue"><i class="far fa-file-alt text-slate-400"></i> Viewing charging history</li>
                        <li class="flex items-center gap-2 hover:text-brand-blue"><i class="far fa-file-alt text-slate-400"></i> Managing payment methods</li>
                    </ul>
                </div>

                <!-- Category 3 -->
                <div class="bg-white p-8 rounded-3xl shadow-sm border border-slate-200/60 hover:shadow-lg transition-all duration-300 group cursor-pointer">
                    <div class="w-14 h-14 bg-indigo-500/10 rounded-2xl flex items-center justify-center text-indigo-500 mb-6 group-hover:bg-indigo-500 group-hover:text-white transition-colors duration-300">
                        <i class="fas fa-tools text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Troubleshooting</h3>
                    <p class="text-slate-600 mb-6">Solutions to common issues and error codes you might encounter.</p>
                    <ul class="space-y-3 text-sm font-medium text-slate-600">
                        <li class="flex items-center gap-2 hover:text-brand-blue"><i class="far fa-file-alt text-slate-400"></i> Station is offline</li>
                        <li class="flex items-center gap-2 hover:text-brand-blue"><i class="far fa-file-alt text-slate-400"></i> Cable won't unlock</li>
                        <li class="flex items-center gap-2 hover:text-brand-blue"><i class="far fa-file-alt text-slate-400"></i> Red light blinking</li>
                    </ul>
                </div>
            </div>
        </div>
"""

    with open('knowledge-base.html', 'w', encoding='utf-8') as f:
        f.write(header + kb_content + footer)
    print("Created knowledge-base.html")
else:
    print("Could not parse premium-components.html properly")
