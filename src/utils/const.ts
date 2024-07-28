const options = {
    height: 1000,
    duration: 700,
    backgroundColor: "#2F2D2F",
    soundEnable: true,
    // set to true to show outline on open (true|false)
    autoEnableOutline: false,
    // set to true to show thumbnail on open (true|false)
    autoEnableThumbnail: false,
    // set to true if PDF inbuilt outline is to be removed (true|false)
    overwritePDFOutline: false,
    // enableDownload of PDF files (true|false)
    enableDownload: true,
    //direction of flipbook
    //DFLIP.DIRECTION.LTR or 1 for left to right(default),
    //DFLIP.DIRECTION.RTL or 2 for right to left,
    direction: DFLIP.DIRECTION.LTR,
    //set as
    //DFLIP.PAGE_MODE.AUTO for auto-detect(default),
    //DFLIP.PAGE_MODE.SINGLE or 1 for singleview,
    //DFLIP.PAGE_MODE.DOUBLE or 2 for doubleview,
    pageMode: DFLIP.PAGE_MODE.AUTO,
    //set as
    //DFLIP.SINGLE_PAGE_MODE.AUTO for auto-detect(default),
    //DFLIP.SINGLE_PAGE_MODE.ZOOM or 1 for normal zoom single view,
    //DFLIP.SINGLE_PAGE_MODE.BOOKLET or 2 for Booklet mode,
    singlePageMode: DFLIP.SINGLE_PAGE_MODE.AUTO,

    forceFit: true, //very rare usage leave it as true unless page are not fitting wrong...
    transparent: true, //true or false
    hard: "none", //possible values are "hard", "none", "cover"
    //valid controlnames:
    //altPrev,pageNumber,altNext,outline,thumbnail,zoomIn,zoomOut,fullScreen,share
    //more,download,pageMode,startPage,endPage,sound
    allControls: "altPrev,pageNumber,altNext,zoomIn,zoomOut,fullScreen,download,pageMode,startPage,endPage,sound",
    moreControls: "download,pageMode,startPage,endPage,sound",
    hideControls: "",
    controlsPosition: DFLIP.CONTROLSPOSITION.BOTTOM,
    paddingTop: 0,
    paddingLeft: 10,
    paddingRight: 10,
    paddingBottom: 0,
    //set if the zoom changes on mouse scroll (true|false)
    scrollWheel: true,
    // callbacks
    onCreate: function(flipBook) {
        // after flip book is created is fired
        console.log("on create pdf book");
    },
    onCreateUI: function(flipBook) {
        // after ui created event is fired
    },
    onFlip: function(flipBook) {
        // after flip event is fired
    },
    beforeFlip: function(flipBook) {
        // before flip event is fired
    },
    onReady: function(flipBook) {
        // after flip book is completely loaded
    },
    zoomRatio: 1.5,
    pageSize: DFLIP.PAGE_SIZE.AUTO,
};
export default options;