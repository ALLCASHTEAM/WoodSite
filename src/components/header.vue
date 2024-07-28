<template>
  <header class="header">
    <div class="logo">
      <img src="@/assets/logo.jpg" alt="Логотип компании" />
      <h1>WOODSHOP</h1>
    </div>
    <nav class="flex-container">
      <router-link to="/" class="nav-link btn-2" exact-active-class="active">
        Главная
      </router-link>
      <router-link to="/about" class="nav-link btn-2" active-class="active">
        О нас
      </router-link>
      <router-link to="/catalog" class="nav-link btn-2" active-class="active">
        Каталог
      </router-link>
      <router-link to="/contacts" class="nav-link btn-2" active-class="active">
        Контакты
      </router-link>
      <router-link to="/faq" class="nav-link btn-2" active-class="active">
        FAQ
      </router-link>
      <span class="icon btn-2">👤</span>
      <span class="icon btn-2">🛒</span>
    </nav>
  </header>
</template>

<style scoped>
.header {
  font-family: Inter;
  font-size: large;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff8e7;
  border-bottom: 1px solid #ccc;
  padding: 0 20px;
}

.logo {
  display: flex;
  align-items: center;
}

.logo img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}

.flex-container {
  display: flex;
  gap: 20px;
  padding-right: 1%;
}

.nav-link {
  color: inherit;
  text-decoration: none;
  font-size: 22px;
  padding: 10px 20px;
  position: relative;
}

.icon {
  font-size: 24px;
  padding: 10px;
  cursor: pointer;
  position: relative;
}

.btn-2:before,
.btn-2:after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  background: #000;
  transition: width 0.25s ease-in-out;
}

.btn-2:before {
  top: 0;
  left: 0;
}

.btn-2:after {
  bottom: 0;
  right: 0;
}

.btn-2:hover:before,
.btn-2:hover:after {
  width: 100%;
}

.active {
  border-top: 2px solid black;
  border-bottom: 2px solid black;
}
.active:before,
.active:after {
  width: 100% !important;
  background: #fff;
}

.active:hover:before,
.active:hover:after {
  width: 100% !important;
}
</style>
