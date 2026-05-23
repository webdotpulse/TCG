import re

with open('premium-components.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The fancy sections to add
fancy_sections = """

        <!-- Fancy Feature Grid -->
        <section class="max-w-7xl mx-auto mt-24">
            <div class="text-center mb-16">
                <span class="text-brand-blue font-semibold tracking-wider uppercase text-sm mb-2 block">Our Capabilities</span>
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900">Advanced features for power users</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Feature 1 -->
                <div class="bg-white p-8 rounded-3xl shadow-sm border border-slate-200/60 hover:shadow-lg transition-shadow duration-300 group">
                    <div class="w-14 h-14 bg-brand-blue/10 rounded-2xl flex items-center justify-center text-brand-blue mb-6 group-hover:scale-110 transition-transform duration-300">
                        <i class="fas fa-chart-pie text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Deep Analytics</h3>
                    <p class="text-slate-600 leading-relaxed">Gain comprehensive insights into your charging network performance with our advanced reporting dashboard.</p>
                </div>
                <!-- Feature 2 -->
                <div class="bg-white p-8 rounded-3xl shadow-sm border border-slate-200/60 hover:shadow-lg transition-shadow duration-300 group">
                    <div class="w-14 h-14 bg-brand-teal/10 rounded-2xl flex items-center justify-center text-brand-teal mb-6 group-hover:scale-110 transition-transform duration-300">
                        <i class="fas fa-shield-alt text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Enterprise Security</h3>
                    <p class="text-slate-600 leading-relaxed">Bank-grade encryption and secure access controls ensure your infrastructure remains protected at all times.</p>
                </div>
                <!-- Feature 3 -->
                <div class="bg-white p-8 rounded-3xl shadow-sm border border-slate-200/60 hover:shadow-lg transition-shadow duration-300 group">
                    <div class="w-14 h-14 bg-indigo-500/10 rounded-2xl flex items-center justify-center text-indigo-500 mb-6 group-hover:scale-110 transition-transform duration-300">
                        <i class="fas fa-bolt text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Smart Routing</h3>
                    <p class="text-slate-600 leading-relaxed">Intelligent load balancing and dynamic routing optimize energy distribution across all your stations.</p>
                </div>
            </div>
        </section>

        <!-- Testimonials -->
        <section class="max-w-7xl mx-auto mt-24 mb-12">
            <div class="bg-slate-900 rounded-[2.5rem] p-12 lg:p-16 relative overflow-hidden">
                <div class="absolute top-0 right-0 -mt-20 -mr-20 w-80 h-80 bg-brand-blue/20 rounded-full blur-3xl"></div>
                <div class="absolute bottom-0 left-0 -mb-20 -ml-20 w-80 h-80 bg-brand-teal/20 rounded-full blur-3xl"></div>

                <div class="relative z-10 text-center max-w-3xl mx-auto">
                    <i class="fas fa-quote-left text-4xl text-brand-blue mb-8 opacity-50"></i>
                    <p class="text-2xl md:text-3xl text-white font-medium leading-relaxed mb-8">
                        "The Charge Grid has completely transformed how we manage our corporate fleet. The insights and control we now have are unprecedented."
                    </p>
                    <div class="flex items-center justify-center gap-4">
                        <div class="w-12 h-12 bg-slate-700 rounded-full flex items-center justify-center text-white font-bold text-xl">
                            JD
                        </div>
                        <div class="text-left">
                            <h4 class="text-white font-bold">Jane Doe</h4>
                            <p class="text-slate-400 text-sm">Director of Operations, TechCorp</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

# Find the last </main> and inject before it
parts = content.rsplit('</main>', 1)
if len(parts) == 2:
    new_content = parts[0] + fancy_sections + '\n    </main>' + parts[1]
    with open('premium-components.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated premium-components.html")
else:
    print("Could not find </main> tag")
