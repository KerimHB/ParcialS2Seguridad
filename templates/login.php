<!doctype html>
<html lang="en">

<head>
    <title>DarkBook</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS v5.2.1 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="../static/css/style.css" />

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous">
    </script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js" integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz" crossorigin="anonymous">
    </script>
</head>


<body>
    <header>
        <nav class="navbar bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand text-white">
                    <b>DarkBook</b>
                </a>
                <form class="d-flex" action="" method="post">
                    <input class="form-control me-2" name="user" type="text" placeholder="Nombre de usuario" />
                    <input class="form-control me-2" name="pass" type="password" placeholder="Contraseña" />
                    <input class="btn btn-primary  btn-block" type="submit" name="log" value="Sing In" />
                </form>
            </div>
        </nav>
    </header>
    <section class="">
        <div class="container py-5 h-100">
            <div class="row d-flex align-items-center justify-content-center h-100">
                <div class="col-md-8 col-lg-7 col-xl-6">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.svg" class="img-fluid" alt="Phone image">
                </div>
                <div class="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
                    <form action="" method="post">
                        <!-- Email input -->
                        <div class="form-outline mb-4">
                            <label class="form-label" for="form1Example13">Nombre de usuario</label>
                            <input class="form-control form-control-lg me-2" name="user" type="text" placeholder="Nombre de usuario" />
                        </div>

                        <!-- Password input -->
                        <div class="form-outline mb-4">
                            <label class="form-label" for="form1Example23">Password</label>
                            <input class="form-control form-control-lg me-2" name="pass" type="password" placeholder="Contraseña" />
                        </div>

                        <div class="d-flex justify-content-around align-items-center mb-4">
                        </div>

                        <!-- Submit button -->
                        <div class="d-flex justify-content-around align-items-center mb-4">
                            <input class="btn btn-primary btn-lg btn-block" type="submit" name="log" value="Sing In">
                        </div>

                        <div class="divider d-flex align-items-center my-4">
                            <p class="text-center fw-bold mx-3 mb-0 text-muted">OR</p>
                        </div>

                        <div class="row divider d-flex align-items-center my-4">
                            <div class="col-md-6 divider d-flex align-items-center">
                                <a class="btn btn-primary btn-lg btn-block" style="background-color: #3b5998" href="#!" role="button">
                                    <i class="fab fa-facebook-f me-2"></i>Continuar con GitHub
                                </a>
                            </div>
                            <div class="col-md-6 divider d-flex align-items-center">
                                <a class="btn btn-primary btn-lg btn-block " style="background-color: #55acee" href="#!" role="button">
                                    <i class="fab fa-twitter me-2"></i>Continuar con Token
                                </a>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <footer class="container-fjuid text-white text-center bg-dark">
        <div>
            Kerim Michael Hernández Borja
        </div>
    </footer>
</body>


</html>