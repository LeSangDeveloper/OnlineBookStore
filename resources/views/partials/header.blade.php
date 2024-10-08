<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="{{ route('product.index') }}">LS Bookstore</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <form action="{{route('search')}}" method="post" class="navbar-form navbar-left">
        <div class="form-group">
          <input type="text" class="form-control" name="search" placeholder="Type title of book">
        </div>
        <button type="submit" class="btn btn-default">Search</button>
        {{ csrf_field() }}
     </form>
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav navbar-right">
        <li><a href="{{route('product.shoppingcart')}}"><i class="fa fa-shopping-cart"></i>
        Shopping cart <span class="badge"> {{ Session::has('cart')?Session::get('cart')->totalQty:'' }} </span>
      </a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-users"></i> User <span class="caret"></span></a>
          <ul class="dropdown-menu">
            @if(Auth::check())
            <li><a href="#"> Profile </a></li>
            @if(Session::has('admin'))
              @if(Session::get('admin'))
               <li><a href="{{ route('admin.index') }}"> Admin </a></li> 
              @endif
            @endif
            <li role="separator" class="divider"></li>
            <li><a href="{{route('user.logout')}}"> Log Out </a></li>
            @else
            <li><a href="{{route('user.signup')}}"> Sign Up </a></li>
            <li><a href="{{route('user.signin')}}"> Sign In </a></li>
            @endif
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>