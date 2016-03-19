let exampleState = {
    offersIdsForTracker: {
        0: [0, 1],
        1: [2]
    },
    offers: {
        0: {},
        1: {},
        2: {}
    },
    trackers: {
        0: {},
        1: {}
    }
};
/*
 * API calls
 */
export const CREATE_TRACKER = 'CREATE_TRACKER';
export const TRACKER_CREATED = 'TRACKER_CREATED';

export const LIST_TRACKERS = 'LIST_TRACKERS';
export const TRACKERS_LISTED = 'TRACKERS_LISTED';

export const LIST_OFFERS_FOR_TRACKER = 'LIST_OFFERS_FOR_TRACKER';
export const OFFERS_FOR_TRACKER_LISTED = 'OFFERS_FOR_TRACKER_LISTED';

/*
 * other constants
 */

export const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER';
export const VisibilityFilters = {
    SHOW_ALL: 'SHOW_ALL',
    SHOW_COMPLETED: 'SHOW_COMPLETED',
    SHOW_ACTIVE: 'SHOW_ACTIVE'
};

export const HOST = '//localhost:5000';

export function listTrackers() {
    return {
        type: LIST_TRACKERS
    }
}

export function trackersListed(trackers) {
    console.log('trackersListed', trackers);
    return {
        type: TRACKERS_LISTED,
        trackers: trackers,
        receivedAt: Date.now()
    }
}
/*
 * action creators
 */

export function fetchTrackers() {
    return dispatch => {
        dispatch(listTrackers());

        return fetch(`${HOST}/trackers`)
            .then(response => response.json())
            .then(json => {
                    console.log('fetchTrackers done', json);
                    return dispatch(trackersListed(json));
                }
            )
    }
}

export function listOffersForTracker(trackerId) {
    return { type: LIST_OFFERS_FOR_TRACKER, payload: trackerId}
}

export function setVisibilityFilter(filter) {
    return { type: SET_VISIBILITY_FILTER, filter }
}
