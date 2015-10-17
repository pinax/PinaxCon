window.jQuery = window.$ = require("jquery");

require("bootstrap");

require("../less/site.less");

var loadEditors = function () {
    var $editors = $(".modal-body textarea, #id_body, #id_comment, #id_message, #id_text, #id_abstract, #id_additional_notes, #id_content_override, #id_description, #id_biography");
    $editors.each(function (i, el) {
      var editorId = "markdown-editor-" + i,
          reportDiv = $("<div>").attr("id", editorId),
          setupEditor = function (editor, textarea) {
              var session = editor.getSession();
              editor.setTheme("ace/theme/tomorrow");
              editor.$blockScrolling = Infinity;
              editor.setOption("scrollPastEnd", true);
              session.setMode("ace/mode/markdown");
              session.setValue(textarea.val());
              session.setUseWrapMode(true);
              session.on('change', function(){
                textarea.val(session.getValue());
              });
              editor.renderer.setShowGutter(false);
              session.setTabSize(4);
              session.setUseSoftTabs(true);
          },
          $formGroup = $(el).closest(".form-group"),
          $textarea = $formGroup.find("textarea");
      $formGroup.append(reportDiv);
      setupEditor(ace.edit(editorId), $textarea);
      console.log(i, el, $formGroup, $textarea);
    });
};


$(function () {
  loadEditors();
});
