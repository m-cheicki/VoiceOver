"use strict";(self.webpackChunkvoice_over_front=self.webpackChunkvoice_over_front||[]).push([[718],{9718:(J,d,o)=>{o.r(d),o.d(d,{TttModule:()=>q});var h=o(9808),s=o(2382),T=o(1787),A=o(5861),C=o(4464),t=o(4893),y=o(5830),m=o(4594),u=o(4106),c=o(4107),M=o(508),Z=o(7531);const S=[{path:"",component:(()=>{class n{constructor(e){this._tttService=e,this.textToTranslate="",this.translatedText="",this._providerSelected=null,this._languageSelected=null}_initTranslation(){var e=this;return(0,A.Z)(function*(){var a,r,l,g;const v=null!==(a=e.textToTranslate)&&void 0!==a?a:"",p=null!==(r=e._providerSelected)&&void 0!==r?r:null,f=null!==(l=e._languageSelected)&&void 0!==l?l:null;if(v.length<=0||null==p||null==f)return void(e.translatedText="");const x=e._tttService.translate(v,p,f,void 0),U=yield(0,C.n)(x);e.translatedText=null!==(g=U.translation)&&void 0!==g?g:""})()}onKeyUp(){clearTimeout(this._timeoutId),this._timeoutId=setTimeout(()=>{this._initTranslation()},300)}onSelectProvider(e){this._providerSelected=e,this._initTranslation()}onSelectLanguage(e){this._languageSelected=e,this._initTranslation()}}return n.\u0275fac=function(e){return new(e||n)(t.Y36(y.D7))},n.\u0275cmp=t.Xpm({type:n,selectors:[["app-ttt-page"]],decls:37,vars:2,consts:[[1,"mb-3"],[1,"row"],[1,"col"],["appearance","fill",1,"w-100"],["disabled",""],["value","option"],["appearance","outline",1,"w-100"],["matInput","","placeholder","Write some text...","rows","17",1,"textarea",3,"ngModel","ngModelChange","keyup"],[3,"valueChange"],["value","ibm"],["value","google"],["value","en"],["value","fr"],["value","es"],["matInput","","placeholder","Translation will show here","rows","17","readonly","",1,"textarea",3,"ngModel"]],template:function(e,a){1&e&&(t.TgZ(0,"mat-toolbar",0),t.TgZ(1,"span"),t._uU(2,"Translation"),t.qZA(),t.qZA(),t.TgZ(3,"div",1),t.TgZ(4,"div",2),t.TgZ(5,"mat-form-field",3),t.TgZ(6,"mat-label"),t._uU(7,"Auto detect"),t.qZA(),t.TgZ(8,"mat-select",4),t.TgZ(9,"mat-option",5),t._uU(10,"Option"),t.qZA(),t.qZA(),t.qZA(),t.TgZ(11,"mat-form-field",6),t.TgZ(12,"textarea",7),t.NdJ("ngModelChange",function(l){return a.textToTranslate=l})("keyup",function(){return a.onKeyUp()}),t.qZA(),t.qZA(),t.qZA(),t.TgZ(13,"div",2),t.TgZ(14,"div",1),t.TgZ(15,"div",2),t.TgZ(16,"mat-form-field",3),t.TgZ(17,"mat-label"),t._uU(18,"Provider"),t.qZA(),t.TgZ(19,"mat-select",8),t.NdJ("valueChange",function(l){return a.onSelectProvider(l)}),t.TgZ(20,"mat-option",9),t._uU(21,"IBM"),t.qZA(),t.TgZ(22,"mat-option",10),t._uU(23,"Google"),t.qZA(),t.qZA(),t.qZA(),t.qZA(),t.TgZ(24,"div",2),t.TgZ(25,"mat-form-field",3),t.TgZ(26,"mat-label"),t._uU(27,"Language"),t.qZA(),t.TgZ(28,"mat-select",8),t.NdJ("valueChange",function(l){return a.onSelectLanguage(l)}),t.TgZ(29,"mat-option",11),t._uU(30,"English"),t.qZA(),t.TgZ(31,"mat-option",12),t._uU(32,"French"),t.qZA(),t.TgZ(33,"mat-option",13),t._uU(34,"Spanish"),t.qZA(),t.qZA(),t.qZA(),t.qZA(),t.qZA(),t.TgZ(35,"mat-form-field",6),t._UZ(36,"textarea",14),t.qZA(),t.qZA(),t.qZA()),2&e&&(t.xp6(12),t.Q6J("ngModel",a.textToTranslate),t.xp6(24),t.Q6J("ngModel",a.translatedText))},directives:[m.Ye,u.KE,u.hX,c.gD,M.ey,Z.Nt,s.Fj,s.JJ,s.On],styles:["[_nghost-%COMP%]{display:block}textarea[_ngcontent-%COMP%]{resize:none}"]}),n})()}];let P=(()=>{class n{}return n.\u0275fac=function(e){return new(e||n)},n.\u0275mod=t.oAB({type:n}),n.\u0275inj=t.cJS({imports:[[T.Bz.forChild(S)],T.Bz]}),n})(),q=(()=>{class n{}return n.\u0275fac=function(e){return new(e||n)},n.\u0275mod=t.oAB({type:n}),n.\u0275inj=t.cJS({imports:[[h.ez,s.u5,P,m.g0,Z.c,u.lN,c.LD]]}),n})()}}]);