<?php

namespace App\Http\Controllers;

use App\Product;

use App\Cart;

use App\Order;

use Illuminate\Http\Request;

use App\Http\Requests;

use Auth;

use Session;

class ProductController extends Controller
{
    //
    public function getIndex()
    {
    	$products = Product::all();
    	return view('shop.index', ['products' => $products]);
 
    }

    public function getAddToCart(Request $request, $id)
    {
    	$product = Product::find($id);
    	if ($product->inStock > 0)
    	{
    		$product->inStock -= 1;
    		$oldCart = Session::has('cart')?Session::get('cart'):null;
    	
    		$cart = new Cart($oldCart);
    		$cart->add($product, $product->id);

    		$request->session()->put('cart', $cart);
    		$product->save();
    		return redirect()->route('product.index');
		}
		else 
			return redirect()->route('product.index');
	}

    public function getShoppingCart()
    {
        if (!Session::has('cart'))
            return view('user.shopping-cart');

        $oldCart = Session::get('cart');
        $cart = new Cart($oldCart);
        $totalPrice = $cart->totalPrice;
        return view('user.shopping-cart', ['products' => $cart->items, 'totalPrice' => $totalPrice]);
    }

    public function getCheckout()
    {
        return view('user.checkout');
    }

    public function postCheckout(Request $request)
    {
                if(!Session::has('cart'))
        {
            return view('shop.index');
        }
        
        $oldCart = Session::get('cart');
        $cart = new Cart($oldCart);
        
        $order = new Order();
        $order->cart = serialize($cart);
        $order->name = $request->input('name-order');
        $order->address = $request->input('address');

       if(!Auth::check())
            return redirect()->route('user.signin');    
        
        Auth::user()->orders()->save($order);

        Session::forget('cart');
        return redirect()->route('product.index')->with('success', 'Successfully purchased products!');
    }

    public function getRemoveOne(Request $request, $id)
    {
        $oldCart = Session::has('cart')?Session::get('cart'):null;
        $cart = new Cart($oldCart);
        $product = Product::find($id);
        $product->inStock += 1;
        $product->save();
        $cart->removeOne($id);

        Session()->put('cart', $cart);

        $oldCart = Session::get('cart');
        $cart = new Cart($oldCart);
        $totalPrice = $cart->totalPrice;

        if($totalPrice <= 0.0) Session::forget('cart');
        return view('user.shopping-cart', ['products' => $cart->items, 'totalPrice' => $totalPrice]);
    }

    public function getRemoveAll(Request $request, $id)
    {
        $oldCart = Session::has('cart')?Session::get('cart'):null;
        $cart = new Cart($oldCart);
        $product = Product::find($id);
        $product->inStock += $cart->items[$id]['Qty'];
        $product->save();
        $cart->removeAll($id);

        Session()->put('cart', $cart);

        $oldCart = Session::get('cart');
        $cart = new Cart($oldCart);
        $totalPrice = $cart->totalPrice;

        if($totalPrice <= 0.0) Session::forget('cart');
        return view('user.shopping-cart', ['products' => $cart->items, 'totalPrice' => $totalPrice]);
    }
}
