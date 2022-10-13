import { BackendService } from "./backend.service";
import { CatalogueEntry, LayerSubscription } from './backend.api';

const DUMMY_CATALOGUE_ENTRIES: Array<CatalogueEntry> = [
  {
    number: 'LS0000001',
    name: 'Hotspots (Firewatch)',
    description: 'hotspots over last 72 hours. Mapped and updated every 2-4 hours. Hotspots are mapped from MODIS, ' +
      'VIIRS imagery and NOAA imagery provide access to the relevant image data from where the Fire Hot Spots (FHS) ' +
      'used in the product were derived, so factors such as cloud cover and satellite overpass extents can be ' +
      'understood and considered when interpreting the fire hotspots displayed. Resolution is 1km. Accuracy is +/-2km',
    custodian: 'Landgate',
    status: 'draft',
    lastUpdated: '10/02/2022',
    time: '1000',
    assignedTo: 'Rodney Sales',
  }
];
const DUMMY_LAYER_SUBSCRIPTIONS: Array<LayerSubscription> = [
  {
    number: 'LS0000001',
    name: 'Hotspots (Firewatch)',
    description: 'hotspots over last 72 hours. Mapped and updated every 2-4 hours. Hotspots are mapped from MODIS, ' +
      'VIIRS imagery and NOAA imagery provide access to the relevant image data from where the Fire Hot Spots (FHS) ' +
      'used in the product were derived, so factors such as cloud cover and satellite overpass extents can be ' +
      'understood and considered when interpreting the fire hotspots displayed. Resolution is 1km. Accuracy is +/-2km',
    refreshFrequencyMinutes: 5,
    subscribedDate: '10/02/2022',
    subscribedTime: 1000,
    webserviceUrl: 'https://services.slip.wa.gov.au/',
    status: 'active'
  }
];

export class BackendServiceStub implements BackendService {
  public getLayerSubscriptions (): Array<LayerSubscription> {
    return DUMMY_LAYER_SUBSCRIPTIONS;
  }

  public getCatalogueEntries (): Array<CatalogueEntry> {
    return DUMMY_CATALOGUE_ENTRIES;
  }
}
