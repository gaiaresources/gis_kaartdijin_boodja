<script lang="ts" setup>
  import { toCamelCase } from '../../util/strings';

  const { name, value, placeholder, type } = defineProps<{
    name: string,
    value: string,
    placeholder?: string,
    type: string
  }>();

  const emit = defineEmits<{
    (e: 'value-updated', name: string, value: string): void
  }>()
</script>

<template>
  <div class="form-floating">
    <input :id="`${toCamelCase(name)}Input`" :type="type" class="form-control w-auto" placeholder="placeholder"
           @change="(event) => emit('value-updated', name, event.target.value)">
    <label :for="`${toCamelCase(name)}Input`">{{ name }}</label>
  </div>
</template>
