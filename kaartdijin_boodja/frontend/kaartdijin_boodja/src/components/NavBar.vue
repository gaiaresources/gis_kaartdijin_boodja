<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav d-flex w-100 mb-2 mb-lg-0">
          <li class="nav-item align-self-start">
            <a class="nav-link" href="#">Catalogue</a>
          </li>
          <li class="nav-item align-self-start me-auto">
            <a class="nav-link" href="#">Publish</a>
          </li>
          <li class="nav-item align-self-end">
            <a class="nav-link" href="#">Welcome <span class="username-text">Rodney</span></a>
          </li>
          <li class="nav-item align-self-end dropdown">
            <a id="optionsDropdown" class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Options
            </a>
            <ul class="dropdown-menu" aria-labelledby="optionsDropdown">
              <li>
                <a class="dropdown-item" href="#">Settings</a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style lang="scss" scoped>
  .username-text {
    font-weight: bolder;
  }
</style>
