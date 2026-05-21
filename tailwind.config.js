/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./js/**/*.js"],
  theme: {
    extend: {
      colors: {
        'mp-teal': '#009c9e',
        'mp-teal-light': '#019d9f',
        'mp-navy': '#0a192f', // typical dark navy for premium contrast
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
