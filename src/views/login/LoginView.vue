<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="10" class="d-flex flex-column align-center">
        <v-avatar size="200">
          <!-- <v-img src="/assets/images/praya_2.png"></v-img> -->
        </v-avatar>
        <v-card class="mx-auto" min-width="400" v-if="errors.length > 0">
          <v-list v-for="(item, i) in errors" :key="i" :value="item" color="primary" rounded="xl">
            <v-list-item-title v-text="item" class="error pl-4"></v-list-item-title>
          </v-list>
        </v-card>
        <v-card class="mx-auto my-8 pl-6 pr-6" elevation="16" min-width="400" style="min-height:350px;">
          <v-card-item>
            <v-card-title>
              登录
            </v-card-title>
          </v-card-item>
          <v-card-text>
            <v-form ref="form" v-model="formValid" @submit.prevent="submitForm">
              <v-text-field placeholder="用户名/手机号码" v-model="formData.email"
                :error-messages="emailErrors" :rules="emailRules" class="mb-2" label="用户名" clearable
                required>
              </v-text-field>
              <v-text-field v-model="formData.password" :rules="passwordRules" :error-messages="passwordErrors"
                label="密码" required placeholder="密码" clearable
                append-inner-icon="mdi-eye" type="password">
              </v-text-field>

              <div class="d-flex justify-space-between align-end">
                <v-checkbox label="记住我"></v-checkbox>
                <v-btn variant="plain" color="primary" @click="reset" class="text-none">
                  重置密码</v-btn>
              </div>
              <v-btn type="submit" color="success" size="large" variant="elevated" class="mb-6 text-none" block>
                登录
              </v-btn>
              <div class="d-flex justify-center align-center mt-6 mb-6">
                还没有账户<v-btn variant="plain" color="primary" @click="gotoSign"
                  class="text-none">创建一个</v-btn>
              </div>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { useCommon } from '@/stores/common';

import { defineComponent, ref, reactive, handleError } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from '../../axios'

export default defineComponent({
  setup() {
    const router = useRouter();

    let errors = ref([]);
    const store = useCommon();
    const form = ref(null);
    const formValid = ref(false);

    // 表单数据
    const formData = reactive({
      email: '',
      password: '',
    });

    // 错误消息
    const emailErrors = ref([]);
    const passwordErrors = ref([]);

    // 验证规则
    const emailRules = [
      (v) => !!v || '用户名没有输入',
      (v) => /.+@.+\..+/.test(v) || '用户名格式不正确',
    ];

    const passwordRules = [
      (v) => !!v || '密码没有输入',
      (v) => v.length >= 6 || '密码长度应该大于 6',
    ];

    return {
      form,
      formValid,
      formData,
      emailRules,
      passwordRules,
      emailErrors,
      passwordErrors,
      store,
      errors
    };
  },
  methods: {
    handleError(error_code: string) {
      const errors_ = error_code.split(",")
      const err_messages = [];
      for (let i = 0; i < errors_.length; i++) {
        err_messages.push(errors_[i])
      }
      return err_messages;
    },
    // 提交表单
    submitForm() {
      this.errors = [];
      this.$refs.form.validate().then((response:any) => {
        console.log(response)
        if (response.valid) {
          axios.get('/api/user/login',
            {
              params: {
                'email': 'data.comment',
                'password': 'password'
              }

            }).then((response) => {
              if (response.data.error_code) {
                this.errors = this.handleError(response.data.error_code)
              } else {
                // 处理提交逻辑
                this.store.setLogin(true);
                this.$router.push({
                  path: "/dashboard"
                })
              }
            }).catch((error) => {
              console.log(error)
            })
        } 
      });
    },

    reset() {
      this.$router.push({
        name: "reset"
      })
    },
    gotoSign() {
      this.$router.push({
        name: "sign"
      })
    },
  },
});
</script>
<style scoped>
</style>