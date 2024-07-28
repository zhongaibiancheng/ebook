<template>
    <v-app-bar color="surface-variant" app>
      <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->
      <v-img src="/assets/images/logo.png" alt="Logo" contain max-height="50" class="mr-2 hover-pointer" @click="backToIndex"></v-img>
      <v-toolbar-title>文档转书</v-toolbar-title>

        <v-spacer></v-spacer>
        <v-btn text @click="goTo('price')">Price</v-btn>
        <v-btn text @click="goTo('about')">About</v-btn>
        <v-btn text @click="goTo('contact')">Contact</v-btn>
        <v-spacer></v-spacer>
        <v-btn text @click="login">Login</v-btn>
        <v-btn outlined @click="signUp">Sign Up</v-btn>
    </v-app-bar>
</template>
<script>
export default {
    name: 'HeaderComponent',
    methods: {
        goTo(page) {
            this.$router.push({ name: page });
        },
        backToIndex(){
          this.$router.push({ name: 'index' });
        },
        login() {
            // Handle login logic here
        },
        signUp() {
            // Handle sign-up logic here
        },
    },
};
</script>
<style scoped>
.hover-pointer{
  pointer:default;
}
.hover-pointer:hover{
  cursor: pointer;
}
</style>