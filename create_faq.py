import re

with open('premium-components.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header and footer using regex
header_match = re.search(r'(.*?)(<main.*?>)', content, re.DOTALL)
footer_match = re.search(r'(</main>.*)', content, re.DOTALL)

if header_match and footer_match:
    header = header_match.group(1) + '<main class="pt-32 pb-24">'

    # Extract the last </main> part, avoiding the ones inside
    parts = content.rsplit('</main>', 1)
    footer = '\n    </main>' + parts[1]

    faq_content = """
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
            <div class="text-center">
                <span class="text-brand-blue font-semibold tracking-wider uppercase text-sm mb-2 block">Help Center</span>
                <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 mb-6 tracking-tight">Frequently Asked Questions</h1>
                <p class="text-lg text-slate-600">Everything you need to know about our charging solutions and services.</p>
            </div>

            <div class="space-y-4">
                <!-- FAQ Item 1 -->
                <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow-md transition-shadow duration-300">
                    <h3 class="text-xl font-bold text-slate-900 mb-3">How fast can I charge my EV?</h3>
                    <p class="text-slate-600">Charging speeds depend on your vehicle's onboard charger and the charging station's capacity. Our premium home chargers typically provide 22kW, adding about 75 miles of range per hour of charging.</p>
                </div>
                <!-- FAQ Item 2 -->
                <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow-md transition-shadow duration-300">
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Do I need a special electrical setup at home?</h3>
                    <p class="text-slate-600">Most homes require a 240V outlet or a hardwired connection installed by a certified electrician. We offer professional installation services to ensure everything is set up safely and correctly according to local regulations.</p>
                </div>
                <!-- FAQ Item 3 -->
                <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow-md transition-shadow duration-300">
                    <h3 class="text-xl font-bold text-slate-900 mb-3">What happens if there's a power outage?</h3>
                    <p class="text-slate-600">Our charging stations have built-in fail-safes. During an outage, charging will pause automatically. Once power is restored, charging resumes without any intervention required from your side.</p>
                </div>
                <!-- FAQ Item 4 -->
                <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow-md transition-shadow duration-300">
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Is your network compatible with all EV models?</h3>
                    <p class="text-slate-600">Yes, our charging points support Type 2 connectors, which are standard across Europe for almost all modern Electric Vehicles, including Tesla, Volkswagen, Audi, and BMW.</p>
                </div>
            </div>

            <div class="bg-slate-900 rounded-3xl p-8 text-center mt-12">
                <h3 class="text-2xl font-bold text-white mb-4">Still have questions?</h3>
                <p class="text-slate-300 mb-6">Can't find the answer you're looking for? Please chat to our friendly team.</p>
                <a href="contact.html" class="inline-block bg-brand-blue hover:bg-blue-600 text-white font-bold py-3 px-8 rounded-xl transition-colors">Contact Support</a>
            </div>
        </div>
"""

    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(header + faq_content + footer)
    print("Created faq.html")
else:
    print("Could not parse premium-components.html properly")
