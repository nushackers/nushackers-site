const spawn = require('child_process').spawn;
const gulp = require('gulp');
const gutil = require('gulp-util');
const changedInPlace = require('gulp-changed-in-place');
const sass = require('gulp-sass');
const notify = require('gulp-notify');
const plumber = require('gulp-plumber');
const postcss = require('gulp-postcss');
const assets  = require('postcss-assets');
const sorting = require('postcss-sorting');
const prettier = require('gulp-prettiest');
const autoprefixer = require('autoprefixer');
const flexbugs = require('postcss-flexbugs-fixes');

const IS_PRODUCTION = !!gutil.env.production;
const IS_DEVELOPMENT = !IS_PRODUCTION;
const SCSS_GLOB = './static/scss/**/*.scss';
const SCSS_ENTRY = './static/scss/main.scss';
const SCSS_PATH = './static/scss';
const CSS_PATH = './static/css';

const sortPlugin = sorting({
  order: [
    'custom-properties',
    'dollar-variables',
    'declarations',
    'rules',
    'at-rules',
  ],
  'properties-order': [
    'content',

    'position',
    'top',
    'right',
    'bottom',
    'left',
    'z-index',

    'display',
    'visibility',
    'opacity',
    'flex',
    'flex-grow',
    'flex-shrink',
    'flex-basis',
    'flex-direction',
    'flex-flow',
    'flex-wrap',
    'align-content',
    'align-items',
    'align-self',
    'justify-content',
    'order',
    'float',
    'clear',
    'box-sizing',
    'width',
    'min-width',
    'max-width',
    'height',
    'min-height',
    'max-height',
    'padding',
    'padding-top',
    'padding-right',
    'padding-bottom',
    'padding-left',
    'margin',
    'margin-top',
    'margin-right',
    'margin-bottom',
    'margin-left',
    'overflow',
    'overflow-x',
    'overflow-y',

    'font',
    'font-style',
    'font-weight',
    'font-size',
    'line-height',
    'font-family',
    'font-variant',
    'text-align',
    'text-decoration',
    'text-shadow',
    'text-transform',
    'white-space',
    'vertical-align',
    'list-style',
    'list-style-position',
    'list-style-type',

    'color',
    'border',
    'border-width',
    'border-style',
    'border-color',
    'border-top',
    'border-top-width',
    'border-top-style',
    'border-top-color',
    'border-right',
    'border-right-width',
    'border-right-style',
    'border-right-color',
    'border-bottom',
    'border-bottom-width',
    'border-bottom-style',
    'border-bottom-color',
    'border-left',
    'border-left-width',
    'border-left-style',
    'border-left-color',
    'border-radius',
    'border-top-left-radius',
    'border-top-right-radius',
    'border-bottom-right-radius',
    'border-bottom-left-radius',
    'background',
    'background-image',
    'background-position',
    'background-position-x',
    'background-position-y',
    'background-size',
    'background-repeat',
    'background-attachment',
    'background-origin',
    'background-clip',
    'background-color',
    'outline',
    'box-shadow',

    'filter',
    'transform',
    'transform-origin',

    'pointer-events',
    'cursor',

    'transition',
    'transition-property',
    'transition-duration',
    'transition-timing-function',
    'transition-delay',
    'animation',
  ],
});

const errorPlugin = () =>
  plumber(function(error) {
    if (IS_DEVELOPMENT) {
      notify.onError({
        title: 'Error on scss',
        message: error.messageFormatted,
        sound: false,
      })(error);
      this.emit('end');
    } else {
      throw error;
    }
  });

// Lints and fixes scss
gulp.task('scss:fix', () => {
  if (IS_PRODUCTION) {
    return;
  }
  return gulp
    .src(SCSS_GLOB)
    .pipe(changedInPlace())
    .pipe(errorPlugin())
    .pipe(postcss([sortPlugin], { syntax: require('postcss-scss') }))
    .pipe(
      prettier({
        parser: 'postcss',
      })
    )
    .pipe(gulp.dest(SCSS_PATH));
});

// Compiles to css and autoprefixes it
gulp.task('scss:compile', ['scss:fix'], () => {
  return gulp
    .src(SCSS_ENTRY)
    .pipe(errorPlugin())
    .pipe(
      sass({
        includePaths: ['node_modules/'],
        outputStyle: IS_PRODUCTION ? 'compressed' : 'nested',
      })
    )
    .pipe(
      postcss([
        assets({
          loadPaths: ['static/'],
        }),
        flexbugs,
        autoprefixer(),
      ])
    )
    .pipe(gulp.dest(CSS_PATH));
});

// Configures styles
gulp.task('styles', () => {
  // Watch style folder for changes
  if (IS_DEVELOPMENT) {
    gulp.watch(SCSS_GLOB, { awaitWriteFinish: true }, ['scss:compile']);
  }
});

// Runs Hugo
gulp.task('hugo', ['scss:compile'], () => {
  const flags = [];
  if (IS_DEVELOPMENT) {
    flags.push('server'); // watch and serve
    flags.push('--navigateToChanged'); // navigate to changed file
  }
  const child = spawn('hugo', flags);

  child.stdout.setEncoding('utf8');
  child.stdout.on('data', data => {
    data
      .split('\n')
      .filter(line => {
        return line.length;
      })
      .forEach(line => {
        gutil.log(line.replace(/\d{4}-.+/, ''));
      });
  });

  child.stderr.setEncoding('utf8');
  child.stderr.on('data', data => {
    const error = new gutil.PluginError({
      plugin: 'Hugo',
      message: data,
    });
    if (IS_DEVELOPMENT) {
      notify.onError({
        title: 'Error on hugo',
        message: error.messageFormatted,
        sound: false,
      })(error);
    } else {
      throw error;
    }
  });
});

gutil.log(
  'Running in',
  IS_PRODUCTION
    ? gutil.colors.magenta('production')
    : gutil.colors.cyan('development'),
  'mode'
);

gulp.task('default', ['hugo', 'styles']);
