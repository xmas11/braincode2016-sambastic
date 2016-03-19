import { combineReducers } from 'redux';
import {
    CREATE_TRACKER,
    TRACKER_CREATED,
    LIST_TRACKERS,
    TRACKERS_LISTED,

    LIST_OFFERS_FOR_TRACKER,
    SET_VISIBILITY_FILTER,
    VisibilityFilters
} from '../actions/actions';
const { SHOW_ALL } = VisibilityFilters;


function visibilityFilter(state = SHOW_ALL, action) {
    switch (action.type) {
        case SET_VISIBILITY_FILTER:
            return action.filter;
        default:
            return state
    }
}

function trackers(state = {}, action) {
    if (action.type === TRACKERS_LISTED) {
        return action.trackers;
    }
    return state;
}
/*
function todos(state = [], action) {
    switch (action.type) {
        case ADD_TODO:
            return [
                ...state,
                {
                    text: action.text,
                    completed: false
                }
            ];
        case COMPLETE_TODO:
            return state.map((todo, index) => {
                if (index === action.index) {
                    return Object.assign({}, todo, {
                        completed: true
                    })
                }
                return todo
            });
        default:
            return state
    }
}
*/

const pricemize = combineReducers({
    visibilityFilter,
    trackers
});

export default pricemize
