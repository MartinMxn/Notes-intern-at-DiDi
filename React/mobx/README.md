## Store 中用
```
import { action, observable } from 'mobx';

class IndexStore {
  @observable upmInfo = [];
  定义init store

  @action setRightVisiable = (visiable) => {
      this.noRightModalVisiable = visiable
    }
  定义function
}


在component上装饰器写
@observer
@inject("IndexStore")
class TimerView extends React.Component {
  this.props.IndexStore.xxx
  //获取obj or function
}
```
