// Use this code for Google Docs, Forms, or new Sheets.
function onOpen() {
  SpreadsheetApp.getUi() // Or DocumentApp or FormApp.
      .createMenu('Dialog')
      .addItem('Open', 'openDialog')
      .addToUi();
}

function openDialog() {
  var html = HtmlService.createHtmlOutputFromFile('index')
      .setSandboxMode(HtmlService.SandboxMode.IFRAME);
  SpreadsheetApp.getUi() // Or DocumentApp or FormApp.
      .showModalDialog(html, 'Dialog title');
}

// Use this code for the older version of Sheets.
function onOpen() {
  var menu = [{name: 'Open', functionName: 'openDialog'}];
  SpreadsheetApp.getActive().addMenu('Dialog', menu);
}

function openDialog() {
  var html = HtmlService.createHtmlOutputFromFile('index')
      .setSandboxMode(HtmlService.SandboxMode.IFRAME);
  SpreadsheetApp.getActive().show(html);
}