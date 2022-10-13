<script lang="ts" setup>
  import DataTable from './DataTable.vue';
  import PlusCircleFill from '../icons/plusCircleFill.vue';
  import { LayerSubscription } from '../../backend/backend.api';
  import CollapsibleRow from './CollapsibleRow.vue';

  const { rows } = defineProps<{
    rows: Array<LayerSubscription>
  }>();
</script>
<template>
  <data-table>
    <template #headers>
      <tr>
        <th></th>
        <th>Number</th>
        <th>Name</th>
        <th>Subscribed Date</th>
        <th>Time</th>
        <th>Webservice Url</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </template>
    <template #data>
      <CollapsibleRow v-for="(row, index) in rows" :id="index">
        <template #cells>
          <td>
            {{ row.number }}
          </td>
          <td>{{ row.name }}</td>
          <td>{{ row.subscribedDate }}</td>
          <td>{{ row.subscribedTime }}</td>
          <td>{{ row.webserviceUrl }}</td>
          <td>{{ row.status }}</td>
          <td>
            <a href="#">View</a>
            <a href="#">History</a>
          </td>
        </template>
        <template #content>
          <td colspan="8">
            <span class="fw-bold small">Catalogue layer description: </span>
            {{ row.description }}
          </td>
        </template>
      </CollapsibleRow>
      <tr>
        <td colspan="8"><PlusCircleFill colour="#4284BC"></PlusCircleFill></td>
      </tr>
    </template>
  </data-table>
</template>
