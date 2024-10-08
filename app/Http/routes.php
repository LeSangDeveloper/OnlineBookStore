<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

Route::get('/', [
	'uses' => 'ProductController@getIndex',
	'as'	=> 'product.index'
]);

Route::post('/search', [
	'uses' => 'ProductController@postIndex',
	'as'	=> 'search'
]);

Route::group(['prefix' => 'admin'], function(){
	Route::group(['middleware'	=>	'CheckAdmin'], function(){
		Route::get('/index', [	
			'uses'	=>	'AdminController@getIndex',
			'as'	=> 'admin.index'
		]);
	

	Route::get('/addProduct', [
			'uses'	=>	'AdminController@getAddProduct',
			'as'	=>	'addproduct'
	]);

	Route::post('/addProduct', [
			'uses'	=>	'AdminController@postAddProduct',
			'as'	=>	'addproduct'
	]);


	Route::get('/update-Product', [
			'uses'	=>	'AdminController@getUpdateProduct',
			'as'	=>	'updateproduct'
	]);

	Route::post('/postupdateProduct', [
			'uses'	=>	'AdminController@postUpdateProduct',
			'as'	=>	'postupdateproduct'
	]);

	Route::get('updateProduct/{id}', [
		'uses'	=>	'AdminController@getUpdateProductId',
		'as'	=>	'product.updateproduct'
	]);
	});
});

Route::group(['prefix'	=>	'user'], function() {

Route::group(['middleware'	=>	'guest'], function(){

	Route::get('/signup', [
		'uses' => 'UserController@getSignup',
		'as'	=> 'user.signup'
	]);

	Route::post('/signup', [
		'uses'	=> 'UserController@postSignup',
		'as'	=> 'user.signup'
	]);

	Route::get('/signin', [
		'uses'	=>	'UserController@getSignin',
		'as'	=>	'user.signin'
	]);

	Route::post('/signin', [
		'uses'	=>	'UserController@postSignin',
		'as'	=>	'user.signin'
	]);

});

Route::group(['middleware'	=>	'auth'], function(){

	Route::get('/logout', [
		'uses'	=>	'UserController@getLogout',
		'as'	=>	'user.logout'
	]);

	Route::get('/AddToCart/{id}', [
		'uses'	=>	'ProductController@getAddToCart',
		'as'	=>	'product.addtocart'
	]);

	Route::get('/shoppingCart', [
		'uses'	=> 'ProductController@getShoppingCart',
		'as'	=>	'product.shoppingcart'
	]);

	Route::get('/checkout', [
		'uses'	=> 'ProductController@getCheckout',
		'as'	=> 'product.checkout'
	]);

	Route::post('/checkout', [
		'uses'	=> 'ProductController@postCheckout',
		'as'	=>	'product.checkout'
	]);
	Route::get('/removeOne/{id}', [
		'uses'	=>	'ProductController@getRemoveOne',
		'as'	=>	'product.removeone'
	]);

	Route::get('/removeAll/{id}', [
		'uses'	=>	'ProductController@getRemoveAll',
		'as'	=>	'product.removeall'
	]);

	Route::post('/add-to-cart/{id}', [
	'uses' => 'ProductController@postAddToCart',
	'as'	=> 'product.addToCart'
]);
});

});