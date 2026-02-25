/**
 * Webnode Compatibility Shim
 * Fixes "wnd is not defined" and related errors by providing empty mocks for missing globals.
 */
// Define wnd object if it doesn't exist
if (typeof wnd === 'undefined') {
    window.wnd = {};
}

// Add common properties that might be accessed
window.wnd.staticDomain = window.location.origin;

// Also mock MVCModelData if expected on global scope
if (typeof MVCModelData === 'undefined') {
    window.MVCModelData = {};
}

console.log("Webnode shim loaded: wnd and MVCModelData defined.");
