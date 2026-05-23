import re

with open('premium-components.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header and footer using regex
header_match = re.search(r'(.*?)(<main.*?>)', content, re.DOTALL)
parts = content.rsplit('</main>', 1)

if header_match and len(parts) == 2:
    header = header_match.group(1) + '<main class="pt-32 pb-24">'
    footer = '\n    </main>' + parts[1]

    jobs_content = """
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-24">

            <!-- Hero Section -->
            <div class="text-center max-w-3xl mx-auto">
                <span class="text-brand-teal font-semibold tracking-wider uppercase text-sm mb-2 block">Careers</span>
                <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 mb-6 tracking-tight">Help us build the future of energy</h1>
                <p class="text-lg text-slate-600">We're looking for passionate individuals to join our mission in creating sustainable, smart charging infrastructure across the globe.</p>
            </div>

            <!-- Culture Section -->
            <div class="bg-white rounded-[2.5rem] shadow-sm border border-slate-200/60 p-12 lg:p-16">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
                    <div>
                        <h2 class="text-3xl font-bold text-slate-900 mb-6">Why join The Charge Grid?</h2>
                        <ul class="space-y-6">
                            <li class="flex gap-4">
                                <div class="w-12 h-12 bg-green-50 rounded-xl flex items-center justify-center text-green-500 shrink-0">
                                    <i class="fas fa-leaf text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-slate-900">Make an impact</h4>
                                    <p class="text-slate-600 text-sm mt-1">Every line of code and every station installed contributes directly to reducing carbon emissions.</p>
                                </div>
                            </li>
                            <li class="flex gap-4">
                                <div class="w-12 h-12 bg-brand-blue/10 rounded-xl flex items-center justify-center text-brand-blue shrink-0">
                                    <i class="fas fa-laptop-house text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-slate-900">Flexible working</h4>
                                    <p class="text-slate-600 text-sm mt-1">Remote-friendly culture with flexible hours. Work from where you're most productive.</p>
                                </div>
                            </li>
                            <li class="flex gap-4">
                                <div class="w-12 h-12 bg-purple-50 rounded-xl flex items-center justify-center text-purple-500 shrink-0">
                                    <i class="fas fa-graduation-cap text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-slate-900">Continuous learning</h4>
                                    <p class="text-slate-600 text-sm mt-1">Generous budget for courses, conferences, and books to keep your skills sharp.</p>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <div class="bg-slate-100 rounded-3xl h-full min-h-[300px] relative overflow-hidden flex items-center justify-center">
                         <div class="absolute inset-0 bg-gradient-to-br from-brand-blue/20 to-brand-teal/20"></div>
                         <i class="fas fa-users text-8xl text-slate-300 opacity-50 relative z-10"></i>
                    </div>
                </div>
            </div>

            <!-- Open Positions -->
            <div>
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-slate-900">Open Positions</h2>
                    <p class="text-slate-600 mt-4">Find your next role.</p>
                </div>

                <div class="max-w-4xl mx-auto space-y-4">
                    <!-- Job 1 -->
                    <a href="#" class="block bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow-md hover:border-brand-blue/50 transition-all duration-300 group">
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                            <div>
                                <h3 class="text-lg font-bold text-slate-900 group-hover:text-brand-blue transition-colors">Senior Frontend Engineer</h3>
                                <p class="text-slate-500 text-sm mt-1">Engineering &middot; Full-time &middot; Remote (EU)</p>
                            </div>
                            <span class="text-brand-blue font-semibold text-sm group-hover:translate-x-1 transition-transform inline-flex items-center gap-1">Apply Now <i class="fas fa-arrow-right text-xs"></i></span>
                        </div>
                    </a>

                    <!-- Job 2 -->
                    <a href="#" class="block bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow-md hover:border-brand-blue/50 transition-all duration-300 group">
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                            <div>
                                <h3 class="text-lg font-bold text-slate-900 group-hover:text-brand-blue transition-colors">Backend Developer (Node.js/Python)</h3>
                                <p class="text-slate-500 text-sm mt-1">Engineering &middot; Full-time &middot; Hybrid (Berlin)</p>
                            </div>
                            <span class="text-brand-blue font-semibold text-sm group-hover:translate-x-1 transition-transform inline-flex items-center gap-1">Apply Now <i class="fas fa-arrow-right text-xs"></i></span>
                        </div>
                    </a>

                    <!-- Job 3 -->
                    <a href="#" class="block bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow-md hover:border-brand-blue/50 transition-all duration-300 group">
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                            <div>
                                <h3 class="text-lg font-bold text-slate-900 group-hover:text-brand-blue transition-colors">Customer Success Specialist</h3>
                                <p class="text-slate-500 text-sm mt-1">Support &middot; Full-time &middot; Remote</p>
                            </div>
                            <span class="text-brand-blue font-semibold text-sm group-hover:translate-x-1 transition-transform inline-flex items-center gap-1">Apply Now <i class="fas fa-arrow-right text-xs"></i></span>
                        </div>
                    </a>
                </div>
            </div>
        </div>
"""

    with open('jobs.html', 'w', encoding='utf-8') as f:
        f.write(header + jobs_content + footer)
    print("Created jobs.html")
else:
    print("Could not parse premium-components.html properly")
