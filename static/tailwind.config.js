module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        "rify-yellow": "#FFC300",
        "rify-title": "#242942",
        "rify-text": "#8E8D8B",
      },
      fontFamily: {
        poppins: "'Poppins', sans-serif",
        lora: "'Lora', serif",
      },
    },
    container: {
      center: true,
      padding: "1rem",
      screens: {
        lg: "960px",
        xl: "1200px",
        "2xl": "1320px",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [require('@tailwindcss/forms')],
}
