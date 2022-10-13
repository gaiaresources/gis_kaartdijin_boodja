<script lang="ts" setup>
  import DataTable from './DataTable.vue';
  import PlusCircleFill from '../icons/plusCircleFill.vue';
  import CollapsibleRow from './CollapsibleRow.vue';
  import { CatalogueEntry } from '../../backend/backend.api';

  const { rows } = defineProps<{
    rows: Array<CatalogueEntry>
  }>();
</script>
<template>
  <data-table>
    <template #headers>
      <tr>
        <th></th>
        <th>Number</th>
        <th>Name</th>
        <th>Custodian</th>
        <th>Status</th>
        <th>Last Updated</th>
        <th>Time</th>
        <th>Assigned To</th>
        <th>Action</th>
      </tr>
    </template>
    <template #data>
      <CollapsibleRow v-for="(row, index) in rows" :id="index">
        <template #cells>
          <td>{{ row.number }}</td>
          <td>{{ row.name }}</td>
          <td>{{ row.custodian }}</td>
          <td>{{ row.status }}</td>
          <td>{{ row.lastUpdated }}</td>
          <td>{{ row.time }}</td>
          <td>{{ row.assignedTo }}</td>
          <td><a href="#">View</a><a href="#">History</a></td>
        </template>
        <template #content>
          <td colspan="8">
            <span class="fw-bold small">Catalogue layer description: </span>{{ row.description }}
          </td>
        </template>
      </CollapsibleRow>
      <tr>
        <td colspan="9"><PlusCircleFill colour="#4284BC"></PlusCircleFill></td>
      </tr>
    </template>
  </data-table>
</template>
