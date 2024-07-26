<template>
  <v-app>
    <HeaderComponent />
        <FooterComponent />
    <v-navigation-drawer app>
    </v-navigation-drawer>
    <v-main>
      <v-container fluid>
        <v-row>
          <v-col>
            <h1>Main Content Area</h1>
            <p>This is where your main content will go.</p>
          </v-col>
        </v-row>
      </v-container>
    </v-main>

  </v-app>
</template>

<script>
import HeaderComponent from '../components/Header.vue';
import FooterComponent from '../components/Footer.vue';

export default {
  name: 'App',
  components: {
    HeaderComponent,
    FooterComponent,
  },
};
</script>

<style>

</style>
