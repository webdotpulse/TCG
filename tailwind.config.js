/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./js/**/*.js"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Dosis', 'sans-serif'],
      },
      colors: {
        brand: {
          blue: '#299FF5',
          teal: '#009C9E',
        },
        secondary: '#0f172a', // Slate 900
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'slide-in-left': 'slideInLeft 0.8s ease-out both',
        'slide-in-right': 'slideInRight 0.8s ease-out both',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-20px)' },
        },
        slideInLeft: {
          '0%': { transform: 'translateX(-50px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        slideInRight: {
          '0%': { transform: 'translateX(50px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        'progress-bar-stripes': {
          'from': { backgroundPosition: '1rem 0' },
          'to': { backgroundPosition: '0 0' }
        }
      }
    }
  },
  plugins: [],
}