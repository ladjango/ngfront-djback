var gulp = require('gulp'),
	path = require('path'),
	sass = require('gulp-sass'),
	sourcemaps = require('gulp-sourcemaps');

var paths = {

	jslibs: [
		'bower_components/angular/angular.min.js',
		'bower_components/angular-resource/angular-resource.min.js',
        'bower_components/angular-route/angular-route.min.js',
        'bower_components/bootstrap/dist/js/bootstrap.min.js',
        'bower_components/jquery/dist/jquery.min.js'
	],

	styles: [
		'bower_components/bootstrap/dist/css/bootstrap.min.css'
	],

	fonts: [
		'bower_components/bootstrap/fonts/**/*'
	],
	
	dest: {
		scripts:   path.join(__dirname, 'static', 'scripts'),
		styles:    path.join(__dirname, 'static', 'styles')
	},
	scss: {
		source: path.join(__dirname, 'source', 'scss/**/*.scss')
	}
}

var sass_error_handler = function(err) {
	console.log(err);
};

gulp.task('copy-styles', function() {
	gulp.src(paths.styles)
		.pipe(gulp.dest(path.join(paths.dest.styles, 'css')));

	gulp.src(paths.fonts)
		.pipe(gulp.dest(path.join(paths.dest.styles, 'fonts')));

});

gulp.task('copy-scripts', function() {
	gulp.src(paths.jslibs)
		.pipe(gulp.dest(paths.dest.scripts));
});

gulp.task('sass', function() {
	gulp.src(paths.scss.source)
		.pipe(sourcemaps.init())
		.pipe(sass().on('error', sass_error_handler))
		.pipe(sourcemaps.write())
		.pipe(gulp.dest(path.join(paths.dest.styles, 'css')));
});

gulp.task('sass:watch', function() {
    gulp.watch(paths.scss.source, ['sass']);
});

gulp.task('default', ['copy-scripts', 'copy-styles', 'sass'])