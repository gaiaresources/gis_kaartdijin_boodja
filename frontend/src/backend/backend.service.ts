import { CatalogueEntry, LayerSubscription } from './backend.api';
import type { PaginationFilter } from './backend.api';

export class BackendService {
  public async getLayerSubscriptions(tableFilter: PaginationFilter): Promise<Array<LayerSubscription>> {
    const resp = await fetch(`/api/layerSubscriptions/`);
    return await resp.json() as Promise<LayerSubscription[]>;
  }

  public async getCatalogueEntries(tableFilter: PaginationFilter): Promise<Array<CatalogueEntry>> {
    const resp = await fetch(`/api/catalogueEntries/`);
    return await resp.json() as Promise<CatalogueEntry[]>;
  }
}
