# Kaartdijin Boodja


## Frontend

### Building and dev server

  #### Installing packages
  Standard fare:
    `npm i` to install and/or appropriately update packages and their dependencies
    `npm ci` to clean install, which installs the exact versions of all packages and dependencies listed in the
    `package-lock.json` file. Using the `ci` flag is deterministic and reproducible.

  #### Building
  `npm build`, Viola!

  #### Development environment
  `npm dev`

### Structure

The frontend is broadly split into 3 layers 
They are:
- `backend`
  - Concerned with fetching raw data from external sources
  - Does little to no processing or data transformation
- `stores` (conceptually 'providers' combined with storage)
  - Transforms the results from the backend into a form more appropriate for storage.
    e.g. two different actions might get and store different subsets of the same `backend` data
  - Returns a composable with the store itself, publicly exposed getters, and actions for the store.
    - The store contains the fetched data and prompts an update of the component when updated
    - Getters fetch data and update the store
      - Equivalent to `computed()`
    - Actions fetch data from the `backend` and mutate the store.
      - Equivalent to component methods
      - They can be asynchronous, meaning they can be `await`'ed
- `components`
  - The views that import the store composables and call getters and actions

Lower layers should not call or use definitions of higher layers.
e.g. the call chain would be `component` --> `store` action --> `backend`
