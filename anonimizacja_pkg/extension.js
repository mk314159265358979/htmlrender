const vscode=require('vscode');
const cp=require('child_process');
const path=require('path');

function runPy(t){
 const p=process.platform==='win32'?'python':'python3';
 const s=path.join(__dirname,'python','anon.py');
 return cp.spawnSync(p,[s],{input:t,encoding:'utf-8'}).stdout;
}

exports.activate=(ctx)=>{
 ctx.subscriptions.push(
  vscode.commands.registerCommand('anonimizacja.runFile',()=>{
   const e=vscode.window.activeTextEditor;
   if(!e)return;
   const t=e.document.getText();
   e.edit(b=>b.replace(new vscode.Range(
    e.document.positionAt(0),
    e.document.positionAt(t.length)
   ),runPy(t)));
  }),
  vscode.commands.registerCommand('anonimizacja.runSelection',()=>{
   const e=vscode.window.activeTextEditor;
   if(!e||e.selection.isEmpty)return;
   const s=e.selection;
   e.edit(b=>b.replace(s,runPy(e.document.getText(s))));
  })
 );
};