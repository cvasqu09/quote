<template>
  <Card class="quote-card" @click="toggleShowDeleteIcon">
    <template #content>
      <div class="p-d-flex p-jc-between">
        <span class="p-mr-3 quote-text">"{{quote}}"</span>
        <transition name="fade">
          <i v-show="showDeleteIcon" class="pi pi-trash trash-icon" @click="deleteQuote()"></i>
        </transition>
      </div>
    </template>
    <template #footer>
      <div class="p-d-flex p-jc-between">
        <span><i class="pi pi-heart"></i> {{likes}}</span>
        <span class="quoter quote-text">-{{quoter}}</span>
      </div>
    </template>
  </Card>
</template>

<script>
import {ref, toRefs} from "@vue/reactivity";
import http from "../utils/http";

export default {
  name: "Quote",
  props: {
    id: {
      type: String,
      required: true,
    },
    likes: {
      type: Number,
      required: false,
      default: 0
    },
    quote: {
      type: String,
      required: true
    },
    quoter: {
      type: String,
      required: true,
      default: 'Unknown'
    },
    allowDelete: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  setup(props, { emit }) {
    const { quote, quoter, id } = toRefs(props)
    const showDeleteIcon = ref(false);

    const toggleShowDeleteIcon = () => {
      showDeleteIcon.value = (!showDeleteIcon.value && props.allowDelete)
    }
    const deleteQuote = async () => {
      console.log('deleting quote with id', id.value);
      try {
        await http.delete(`quote/${id.value}`);
        emit('delete')
      } catch(e) {
        console.log('error deleting', e);
      }
    }

    return {
      quote, quoter, deleteQuote, showDeleteIcon, toggleShowDeleteIcon
    }
  }
}
</script>

<style lang="scss" scoped>
::v-deep .p-card-body {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.fade-enter-from {
  opacity: 0
}

.fade-enter-to {
  opacity: 1
}

.fade-enter-active {
  transition: all 0.3s ease;
}

.fade-leave-from {
  opacity: 1;
}

.fade-leave-to {
  opacity: 0;
}

.fade-leave-active {
  transition: all 0.3s ease;
}

.trash-icon {
  &:hover {
    cursor: pointer;
  }
}

.quote-card {
  min-width: 200px;
  max-width: 500px;

  &:hover {
    cursor: pointer;
    box-shadow: 5px 5px 5px $gray-4;
  }
}

.quoter {
  font-style: italic;
}
</style>
