<script setup lang="ts">
  import DataTable from "./DataTable.vue";
</script>

<template>
  <ul class="nav nav-pills mb-4">
    <li class="nav-item">
      <a class="nav-link" aria-current="page" href="#">Catalogue Entries</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Layer Submissions</a>
    </li>
    <li class="nav-item">
      <a class="nav-link active" href="#">Layer Subscriptions</a>
    </li>
  </ul>
  <div class="card">
    <div class="card-header">
      <h4>Layer Subscriptions</h4>
    </div>
    <div class="card-body">
      <div id="layerSubscriptionAccordion" class="accordion">
        <div class="accordion-item">
          <h2 id="headingFilter" class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFilters" aria-expanded="true" aria-controls="collapseFilters">
              Filters
            </button>
          </h2>
          <div id="collapseFilters" class="accordion-collapse collapse show" aria-labelledby="headingFilter" data-bs-parent="#layerSubscriptionAccordion">
            <div class="accordion-body">
              <form class="form d-flex gap-3">
                <div class="form-floating">
                  <select id="statusSelect" class="form-select form-select-sm w-auto" aria-label="Status select">
                    <option selected>Open this select menu</option>
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                  </select>
                  <label for="statusSelect">Status</label>
                </div>
                <div class="form-floating">
                  <input id="subscribedFromInput" type="date" class="form-control w-auto" placeholder="DD/MM/YYYY">
                  <label for="statusSelect">Subscribed from</label>
                </div>
                <div class="form-floating">
                  <input id="subscribedToInput" type="date" class="form-control w-auto" placeholder="DD/MM/YYYY">
                  <label for="statusSelect">Subscribed to</label>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <DataTable/>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  #layerSubscriptionAccordion {
    .accordion-item {
      .accordion-body .form-floating {
        select, input {
          min-width: 15rem;
        }
      }
    }
  }
</style>
