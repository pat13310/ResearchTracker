module.exports = {
    content: [
        './templates/**/*.html',
        './**/templates/**/*.html',
        './**/*.py',
         './**/*.js',
    ],

    theme: {
        extend: {
            fontFamily: {
                'sans': ['Montserrat', 'sans-serif'] // Ensure fonts with spaces have " " surrounding it.
            },
        },

    },
    plugins: [],
    colors: [],
}
