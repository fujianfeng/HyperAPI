# HyperAPI Changelog

## Version 6

### 6.0.15

- Adding Route `rateModel`
    - Available since HDP 4.2.14
    - POST `/projects/{project_ID}/datasets/rateModel`

### 6.0.14

- Adding Resource `segmentation` and Route `segmentation`
    - Available since HDP 4.2.13
    - POST `/projects/{project_ID}/datasets/segmentation`

### 6.0.13

- Adding Routes `exportCreate` and `exportStream`
    - Available since HDP 4.2.12
    - POST `/projects/{project_ID}/exports`
    - GET `/projects/{project_ID}/exports/{export_ID}/stream`

- Removing Routes `exportAuxData` and `streamAuxData`
    - Superseded by `exportCreate` and `exportStream`

### 6.0.12

- Adding Route `streamAuxData`
    - Available since HDP 4.2.11

### 6.0.11

- Adding Route `ExportFile`
    - Available since HDP 4.2.4
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/exportFile`

 - Fix projectFactory method: getdefault in [project.py](HyperAPI/hyper_api/project.py)
 - Fix project methods: isdefault, created, set_as_default, share_users, share_users_id, share_with_user in [project.py](HyperAPI/hyper_api/project.py)
 - Fix dataset methods: created, set_as_default in [dataset.py](HyperAPI/hyper_api/dataset.py)
 - Fix description method: update in [target.py](HyperAPI/hyper_api/target.py)

### 6.0.10

- Adding Route `updateAuxDataModalities`
    - Available since HDP 4.2.4
    - GET `/projects/{project_ID}/auxdata/modalities/update`
  
### 6.0.9

- Adding Route `getAuxDataModalities`
    - Available since HDP 4.2.4
    - GET `/projects/{project_ID}/auxdata/modalities/query`

- Adding Route `checkAuxDataTreeBranch`
    - Available since HDP 4.2.4
    - POST `/projects/{project_ID}/auxdata/checkTreeBranch`

### 6.0.8

- Fix export models

### 6.0.7

- Adding Route `getForecastMetadata`
    - Available since HDP 4.2.3
    - GET `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/metadata`

- Deprecated route `getForecastTunesMetadata`
    - Starting from HDP 4.2.3
    - Superseded by `getForecastMetadata`

### 6.0.6

- Adding new parameter to api call signature to get the raw response
    - api.System.about(raw_response=True)

### 6.0.5

- Adding Route `getForecastTunesMetadata`
    - Available since HDP 4.2.2
    - GET `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/metadata`

- Adding Route `getForecastTunesModalities`
    - Available since HDP 4.2.2
    - POST `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/modalities`

### 6.0.4

- Adding Route `datasetReshapes.exportSteps`
    - Available since HDP 3.6.1
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/reshapes/exportsteps`

### 6.0.3

- Adding Route `addSharedUsers`
    - Available since HDP 4.2
    - POST `/projects/{project_ID}/shared/add`

- Adding Route `removeSharedUsers`
    - Available since HDP 4.2
    - POST `/projects/{project_ID}/shared/remove`

- Adding Route `clearSharedUsers`
    - Available since HDP 4.2
    - POST `/projects/{project_ID}/shared/clear`

- Adding Route `getRelevantSharedUsers`
    - Available since HDP 4.2
    - GET `/projects/{project_ID}/shared/relevant`

### 6.0.2

- Fix resource iterator
- Add correlations compatibility routes for HyperCube 4.3
 - Adding Route `Correlations.NewCorrelation`
    - Removed since HDP 3.0
    - POST `/projects/{project_ID}/tasks/new`

 - Adding Route `Correlations.GetNewJSONfile`
    - Removed since HDP 3.0
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}`

 - Adding Route `Correlations.GetJSONfile`
    - Removed since HDP 3.0
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/correlation/{correlation_ID}`

 - Adding Route `Correlations.GetNewCSVfile`
    - Removed since HDP 3.0
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export`

 - Adding Route `Correlations.GetCSVfile`
    - Removed since HDP 3.0
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export`

 - Adding Route `Correlations.InitListOfCorrelations`
    - Removed since HDP 3.0
    - GET `/projects/{project_ID}/correlations`

 - Adding Route `Correlations.CreateNewCorrelation`
    - Removed since HDP 3.0
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/correlations`

 - Adding Route `Correlations.RenameNewCorrelation`
    - Removed since HDP 3.0
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/rename`

 - Adding Route `Correlations.retrieveCorrelationsPreview`
    - Removed since HDP 3.0
    - GET `/projects/{project_ID}/correlations/previews`

### 6.0.1

- Added new router 'IoT' containing the routes listed below.

- Adding Route `getAllStreams`
    - Available since HDP 4.1
    - GET `/etl/streams`

- Adding Route `createStream`
    - Available since HDP 4.1
    - POST `/etl/streams` 

- Adding Route `getStream`
    - Available since HDP 4.1
    - GET `/etl/streams/{stream_ID}` 

- Adding Route `updateStream`
    - Available since HDP 4.1
    - POST `/etl/streams/{stream_ID}` 

- Adding Route `deleteStream`
    - Available since HDP 4.1
    - POST `/etl/streams/{stream_ID}/delete`

### 6.0

- Adding _README.md_ and _CHANGELOG.md_ files. 

- Updated file hierarchy for `hdp_api` module : `Route`, `Resource`and `Router` base classes have been moved to the `hdp_api.base` module.

- Session details (coming from the _system/about_ route) are now stored in the `hdp_api.base.Router` instance. Display from the `hyper_api.Api` instance has been changed accordingly. 

- Added properties `available_since` and `removed_since` on `hdp_api.base.Resource` so no resources are created on incompatible HDP versions. 
All resources files have been updated accordingly. 

- Removed `available_since`, `deprecated_since` and `reroute` decorators for `hdp_api.base.Route`. `available_since` is now handled as abstract properties on `hdp_api.routes.Route`.
- Added `removed_since` property on `hdp_api.base.Route`. Routes are not created if the HDP version is equal or above that version. This behaviour replaces the `deprecated_since` decorator. 
- Routes compatiblity between HDP versions is no longer managed using the `reroute` decorator but uses the ``hdp_api.base.Route.SubRoute` class which defines variants for the parent route. 
All routes have been updated accordingly.

- Add unittests files to test class methods and behaviour. 

## 5.2 - Refactoring of Projects and Datasets routes

- Deprecated route `DefaultProject`
    - Starting from HDP 3.6
    - Superseded by `updateProject`

- Deprecated route `renameProject`
    - Starting from HDP 3.6
    - Superseded by `updateProject`

## 5.1

### 5.1.11 - Fix variable ignore test

- Adding Route `DefaultResampling`
    - Available since HDP 3.6
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/defaultResampling` 

- Fix variable ignore test in [variable.py](HyperAPI/hyper_api/variable.py)
```
varname = self.name
data = {'updateFields': {varname: {'ignored': True }}}
```


### 5.1.10 - Get RealTime socket configuration

- Adding Resource `Realtime`

- Adding Route `realTimeSocket.getRealTimeSettings`
    - Available since HDP 3.4
    - GET `/realTimeSocket` 


### 5.1.9 - add getModalites api

- Adding Route `getModalites`
    - Available since HDP 3.6
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/modalities`


### 5.1.7 - Nitro Forecast Tunes Stats

- Adding Route `nitro.getForecastTunesStats`
    - Available since HDP 3.5
    - POST `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/stats`

### 5.1.6 - Adding Lasso Model

- Adding Lasso model

### 5.1.5 - 3rd Parties Routes

- Adding Resource `ThirdParties`

- Adding Route `3rdParties.get3rdpartiessettings`
    - Available since HDP 3.4
    - GET `/3rdparties`
### 5.1.4 - Publish to ETL Routes

- Adding Route `DatasetReshapes.publishreshapetoetl`
    - Available since HDP 3.3
    - POST `/projects/{project_ID}/reshapes/{reshape_ID}/etlpublish`

- Adding Route `OptimProcess.publishcontrolcharttoetl`
    - Available since HDP 3.3
    - POST `/optimProcess/projects/{project_ID}/controlCharts/{controlChart_ID}/etlpublish`

### 5.1.3 - Estimate Dataset Size

- Adding Route `Datasets.getEstimate`
    - Available since HDP 3.2
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/estimate`

- Adding Route `Datasets.setEstimate`
    - Available since HDP 3.2
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/estimate`

### 5.1.2 - SWP Matchmaking Get Variable Validation

- Adding Route `Variable.getvariablevalidation`
    - Available since HDP 3.2
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/variables/validation`

- Adding Route `SWPMatchmaking.getoptimizationdetail`
    - GET `/projects/{project_ID}/redeployments/{work_ID}/optimizationDetail`


### 5.1.1 - Get Variable Validation

- Fix API Version number

### 5.1 - Import/Export AuxData Matrices

- Adding Route `AuxData.exportauxdatamatrices`
    - GET `/projects/{project_ID}/auxdata/{auxdata_ID}/exportMatrices/{work_ID}`

- Adding Route `AuxData.importauxdatamatrices`
    - POST `/projects/{project_ID}/auxdata/{auxdata_ID}/importMatrices`
