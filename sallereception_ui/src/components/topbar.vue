<template>
    <nav class="top-bar">
        <div class="top-bar-left nav-desktop">
          <ul class="menu">
            <li>
                <router-link to="/">Gestion de la salle de reception</router-link>
            </li>
          </ul>
        </div>
      
        <div class="top-bar-right nav-desktop">
          <ul class="menu menu-desktop">
            
            <li> 
                <router-link to="/client">Client</router-link> 
            </li>
            <li> 
                <router-link to="/reservation">Reservation</router-link> 
            </li>
            <li> 
                <router-link to="/type_fete">Fete</router-link> 
            </li>
            <li> 
                <router-link to="/type_decor">Decor</router-link> 
            </li>
          </ul>
        </div>
      </nav>
</template>

<script>
</script>

<style scoped>
.menu {
    margin: 0;
    list-style-type: none;
    font-family: sans-serif;}

    .menu > li {
    display: table-cell;
    vertical-align: middle; }

    .menu > li > a {
      display: inline-block;
      padding: 0.7rem 1rem;
      line-height: 1;}

    .menu > li > a {
      color:black;
      text-decoration: none;
      cursor: pointer;
    }

    .menu > li > a:hover {
      color: menu-colour;}
  .top-bar {
      padding: 0.5rem; }

.top-bar::before, .top-bar::after {
    display: table;
    content: ' '; }
  .top-bar::after {
    clear: both; }

.top-bar,.top-bar ul {
    background-color: #e6e6e6; }
  .top-bar-left {
      float: left;
    }

    .top-bar-right {
      float: right;
    
    }
</style>