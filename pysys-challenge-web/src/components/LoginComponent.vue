<template>
  <div class="container">
    <header>
      <h1>Login and Registration Form <span>with HTML5 and CSS3</span></h1>
    </header>
    <div id="container_demo">
      <!-- hidden anchor to stop jump http://www.css3create.com/Astuce-Empecher-le-scroll-avec-l-utilisation-de-target#wrap4  -->
      <div id="wrapper">
        <div id="login" class="animate form">
          <form id="loginForm">
            <h1>Log in</h1>
            <p>
              <label for="username" class="uname" data-icon="u"> Your email or username </label>
              <input id="username" name="username" required="required" type="text"
                     placeholder="myusername or mymail@mail.com"/>
            </p>
            <p>
              <label for="password" class="youpasswd" data-icon="p"> Your password </label>
              <input id="password" name="password" required="required" type="password" placeholder="eg. X8df!90EO"/>
            </p>
            <p class="keeplogin">
              <input type="checkbox" name="loginkeeping" id="loginkeeping" value="loginkeeping"/>
              <label for="loginkeeping">Keep me logged in</label>
            </p>
            <p class="login button">
              <input type="submit" value="Login"/>
            </p>
            <p class="change_link">
              Not a member yet ?
              <a v-bind:href="registration" class="to_register">Join us</a>
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'LoginComponent'
}
</script>
