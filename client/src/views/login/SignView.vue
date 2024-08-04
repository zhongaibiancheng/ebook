<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="10" class="d-flex flex-column align-center">
        <v-avatar size="200">
          <!-- <v-img src="/assets/images/praya_2.png"></v-img> -->
        </v-avatar>
        <v-card class="mx-auto my-8 pl-6 pr-6" elevation="16" min-width="400" style="min-height:350px;">
          <v-card-item>
            <v-card-title>
              创建用户
            </v-card-title>
          </v-card-item>
          <v-card-text>
            <v-form v-model="form" @submit.prevent="onSubmit">
              <v-text-field v-model="email" :readonly="loading" 
              :rules="[required]" class="mb-2" label="邮箱" 
              clearable
              placeholder="输入邮箱"
              >
              </v-text-field>
              <v-text-field v-model="password" :readonly="loading" :rules="[required]" label="密码"
                placeholder="输入密码" clearable append-inner-icon="mdi-eye" type="password">
              </v-text-field>              
              <v-text-field v-model="repassword" :readonly="loading" :rules="[required]" label="确认密码"
                placeholder="输入确认密码" clearable append-inner-icon="mdi-eye" type="password">
              </v-text-field>

              <v-spacer></v-spacer>

              <br>
              <v-btn :disabled="!form" 
              :loading="loading" 
              color="success" 
              size="large" 
              type="submit" 
              variant="elevated"
                class="mb-6" block>
                创建
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const form = ref(false)
const email = ref(null)
const password = ref(null)
const loading = ref(false)

function onSubmit() {
  if (!form.value) return
  loading.value = true
  setTimeout(() => (loading.value = false), 2000)
}
function required(v:any) {
  return !!v || 'Field is required'
}

</script>

<script lang="ts">
export default {
  data: () => ({
    form: false,
    email: null,
    password: null,
    repassword:null,

    loading: false,
  }),

  methods: {
    
  },
}
</script>
<style scoped></style>