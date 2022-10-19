<script lang="ts" setup>
  import { toCamelCase } from '../../util/strings';

  const { name, values } = defineProps<{
    name: string,
    values: Array<string>
  }>();

  const emit = defineEmits<{
    (e: 'value-updated', name: string, value: string): void
  }>()
</script>

<template>
  <div class="form-floating">
    <select :id="`${toCamelCase(name)}Select`" class="form-select form-select-sm w-auto" aria-label="{{ name }} select"
            @change="(event) => emit('value-updated', name, event.target.value)">
      <option :value="null"></option>
      <option v-for="value in values" :value="toCamelCase(name)">{{ value }}</option>
    </select>
    <label :for="`${toCamelCase(name)}Select`">{{ name }}</label>
  </div>
</template>

<style lang="scss">
  select {
    min-width: 7.5rem;
  }
</style>
