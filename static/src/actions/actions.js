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
export const LIST_TRACKERS = 'LIST_TRACKERS';
export const LIST_OFFERS_FOR_TRACKER = 'LIST_OFFERS_FOR_TRACKER';

/*
 * other constants
 */

export const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER';
export const VisibilityFilters = {
    SHOW_ALL: 'SHOW_ALL',
    SHOW_COMPLETED: 'SHOW_COMPLETED',
    SHOW_ACTIVE: 'SHOW_ACTIVE'
};

/*
 * action creators
 */

export function createTracker(tracker) {
    return { type: CREATE_TRACKER, payload: tracker }
}

export function listTrackers() {
    return { type: LIST_TRACKERS }
}

export function listOffersForTracker(trackerId) {
    return { type: LIST_OFFERS_FOR_TRACKER, payload: trackerId}
}

export function setVisibilityFilter(filter) {
    return { type: SET_VISIBILITY_FILTER, filter }
}
