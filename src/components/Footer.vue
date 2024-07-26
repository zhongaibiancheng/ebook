<template>
  <v-footer app>
    <v-container>
      <v-row>
        <v-col class="text-center">
          <span>&copy; {{ new Date().getFullYear() }} My Company</span>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  name: 'FooterComponent',
};
</script>

<style scoped>
v-footer {
  background-color: #3f51b5;
  color: white;
}
</style>
