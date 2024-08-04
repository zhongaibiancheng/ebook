<template>
    <v-container class="full-height">
        <span class="text-h5 font-weight-medium mb-4">请选择套餐</span>
        <div class="mb-4" style="margin-top:-12px;">
            <v-divider :thickness="2" color="info"></v-divider>
        </div>
        <v-row justify="center" align="start">
            <v-col cols="12" md="4" v-for="(plan, index) in plans" :key="index" style="height:70%;">
                <v-card class="equal-height hover-card">
                    <v-card-title class="headline">{{ plan.title }}</v-card-title>
                    <v-card-subtitle>${{ plan.price }}</v-card-subtitle>
                    <v-card-text>
                        <ul>
                            <li v-for="(feature, index) in plan.features" :key="index">{{ feature }}</li>
                        </ul>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="primary" @click="purchase(plan)">Buy Now</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
export default {
    name: 'Price',
    data() {
        return {
            plans: [{
                    title: 'Basic Plan',
                    price: 19.99,
                    features: ['Feature 1', 'Feature 2', 'Feature 3'],
                },
                {
                    title: 'Standard Plan',
                    price: 49.99,
                    features: ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4'],
                },
                {
                    title: 'Premium Plan',
                    price: 99.99,
                    features: ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4', 'Feature 5'],
                },
            ],
        };
    },
    methods: {
        purchase(plan) {
            this.$router.push({

            })
            this.$router.push({ name: 'payment' });
        },
    },
};
</script>
<style scoped>
.headline {
    font-size: 24px;
    font-weight: bold;
}

.full-height {
    height: 100%;
    display: flex;
    flex-direction: column;
}

.equal-height {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 100%;
    padding: 20px;
}

.hover-card {
    transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.hover-card:hover {
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    transform: translateY(-5px);
}
</style>