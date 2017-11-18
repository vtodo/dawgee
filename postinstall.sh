if [ -z "$PRODUCTION" ]; then
    echo Building with debug &&
    browserify --transform coffeeify --debug coffee/main.coffee > dist/js/main.bundle.js
else
    echo Building for production &&
    browserify --transform coffeeify coffee/main.coffee > dist/js/main.bundle.js
fi

if [ -z "$PRODUCTION" ]; then
    echo Would not uglify
else
    echo Would uglify 100%
fi