"use strict";(self.webpackChunkvoice_over_front=self.webpackChunkvoice_over_front||[]).push([[384],{4384:(z,d,n)=>{n.r(d),n.d(d,{TtsModule:()=>A});var f=n(9808),l=n(2382),m=n(1787),v=n(5861),T=n(4464),t=n(4893),y=n(5830),c=n(4594),u=n(4106),g=n(4107),P=n(508),h=n(7531),p=n(7423);const C=["audioPlayer"],Z=[{path:"",component:(()=>{class o{constructor(e){this._ttsService=e,this.text=""}updateAudioPlayer(e){!this.audioPlayer||(this.audioPlayer.nativeElement.src=e.target.result,this.audioPlayer.nativeElement.load())}_initSynthesize(){var e=this;return(0,v.Z)(function*(){if(!e.text||0===e.text.length||!e._provider)return;const a=e._ttsService.synthesize(e.text,e._provider),s=yield(0,T.n)(a),r=new FileReader;r.onload=e.updateAudioPlayer.bind(e),r.readAsDataURL(s.data)})()}synthesize(){clearTimeout(this._timeoutId),this._timeoutId=setTimeout(()=>{this._initSynthesize()},300)}onProviderChange(e){this._provider=e,this.synthesize()}reset(){this.audioPlayer&&(this.audioPlayer.nativeElement.src=""),this.text=""}}return o.\u0275fac=function(e){return new(e||o)(t.Y36(y.kX))},o.\u0275cmp=t.Xpm({type:o,selectors:[["app-tts-page"]],viewQuery:function(e,a){if(1&e&&t.Gf(C,5),2&e){let s;t.iGM(s=t.CRH())&&(a.audioPlayer=s.first)}},decls:19,vars:1,consts:[[1,"mb-3"],["appearance","fill"],[3,"valueChange"],["value","ibm"],["value","google"],["appearance","outline","floatLabel","always",1,"w-100"],["matInput","","placeholder","Enter your text here","rows","20",3,"ngModel","ngModelChange","keyup"],["controls",""],["audioPlayer",""],["type","button","mat-raised-button","","color","primary",1,"mt-3",3,"click"]],template:function(e,a){1&e&&(t.TgZ(0,"mat-toolbar",0),t.TgZ(1,"span"),t._uU(2,"Text to speech"),t.qZA(),t.qZA(),t.TgZ(3,"mat-form-field",1),t.TgZ(4,"mat-label"),t._uU(5,"Provider"),t.qZA(),t.TgZ(6,"mat-select",2),t.NdJ("valueChange",function(r){return a.onProviderChange(r)}),t.TgZ(7,"mat-option",3),t._uU(8,"IBM"),t.qZA(),t.TgZ(9,"mat-option",4),t._uU(10,"Google"),t.qZA(),t.qZA(),t.qZA(),t.TgZ(11,"mat-form-field",5),t.TgZ(12,"mat-label"),t._uU(13,"Text to synthesize"),t.qZA(),t.TgZ(14,"textarea",6),t.NdJ("ngModelChange",function(r){return a.text=r})("keyup",function(){return a.synthesize()}),t.qZA(),t.qZA(),t._UZ(15,"audio",7,8),t.TgZ(17,"button",9),t.NdJ("click",function(){return a.reset()}),t._uU(18,"Reset"),t.qZA()),2&e&&(t.xp6(14),t.Q6J("ngModel",a.text))},directives:[c.Ye,u.KE,u.hX,g.gD,P.ey,h.Nt,l.Fj,l.JJ,l.On,p.lW],styles:["[_nghost-%COMP%]{display:block}[_nghost-%COMP%]   audio[_ngcontent-%COMP%]{width:100%}"]}),o})()}];let M=(()=>{class o{}return o.\u0275fac=function(e){return new(e||o)},o.\u0275mod=t.oAB({type:o}),o.\u0275inj=t.cJS({imports:[[m.Bz.forChild(Z)],m.Bz]}),o})(),A=(()=>{class o{}return o.\u0275fac=function(e){return new(e||o)},o.\u0275mod=t.oAB({type:o}),o.\u0275inj=t.cJS({imports:[[f.ez,l.u5,M,c.g0,u.lN,h.c,g.LD,p.ot]]}),o})()}}]);