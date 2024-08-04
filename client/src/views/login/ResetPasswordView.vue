<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="10" class="d-flex flex-column align-center">
        <v-avatar size="200">
          <!-- <v-img src="/assets/images/praya_2.png"></v-img> -->
        </v-avatar>
        <v-card class="mx-auto my-8 pl-6 pr-6 full-width-card" elevation="16">
          <v-card-item>
            <v-card-title>
              重置密码
            </v-card-title>
          </v-card-item>
          <v-card-text>
            <div class="text-h5 d-flex justify-center text-bold" v-if="step === 1">重置密码链接已经发送到你的邮箱，请确认!</div>
            <v-row justify="center">
              <v-col cols="8" >
                <v-form v-model="form" @submit.prevent="onSubmit" v-if="step === 0">
                  <v-text-field v-model="email" :readonly="loading" :rules="[required]" class="mb-2" label="邮箱"
                    clearable>
                  </v-text-field>
                  <v-btn :disabled="!form" :loading="loading" color="success" size="large" type="submit"
                    variant="elevated" class="mb-6" @click="reset" block>
                    送信
                  </v-btn>
                </v-form>
              </v-col>
            </v-row>

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
const loading = ref(false)

function onSubmit() {
  if (!form.value) return
  loading.value = true
  setTimeout(() => (loading.value = false), 2000)
}
function required(v:any) {
  return !!v || 'Field is required'
}
// function reset(){
//   this.step = 1;
// }
</script>

<script lang="ts">
export default {
  data: () => ({
    form: false,
    email: null,
    loading: false,
    step: 0,//0:reset password 1:邮件发送完毕
  }),

  methods: {
    reset() {
      this.step = 1;
    }
  },
}
</script>
<style scoped>
.full-width-card {
  width: 100%;
  min-height: 350px;
}

.text-bold {
  font-weight: 700;
}
</style>