<script setup lang="ts">
const props = withDefaults(defineProps<{
    contained?: boolean
}>(), {
    contained: false
})
</script>
<template>
    <div class="container" :class="{ contained: props.contained }" role="status" aria-label="Загрузка">
        <div class="circle"/>
    </div>
</template>

<style scoped>
.container {
    display: grid;
    place-items: center;

    min-height: 100dvh;
}

.container.contained {
    min-height: 0;
    width: 100%;
    height: 100%;
}

.circle {
    width: 50px;
    height: 50px;

    box-sizing: border-box;
    border-radius: 100%;

    background-color: var(--color-secondary-90);

    will-change: scale, filter;
    animation: loadingAnimation 1s ease-in-out infinite alternate;
}

@keyframes loadingAnimation {
    from {
        scale: 0.7;
        filter: blur(3px);
    }
    to {
        scale: 1;
        filter: blur(10px);
    }
}
</style>
