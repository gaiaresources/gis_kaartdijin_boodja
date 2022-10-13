<template>
  <div class="table-responsive">
    <table class="table table-bordered table-striped table-hover accordion mb-1">
      <thead>
        <slot name="headers"/>
      </thead>
      <tbody>
        <slot name="data"/>
      </tbody>
    </table>
  </div>
  <span class="ms-2 small fw-bold">Showing 1 to x of y entries</span>
  <nav aria-label="Table navigation" class="d-flex justify-content-end">
    <ul class="pagination">
      <li class="page-item"><a class="page-link" href="#">Previous</a></li>
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item"><a class="page-link" href="#">Next</a></li>
    </ul>
  </nav>
</template>
